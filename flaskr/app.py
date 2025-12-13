import logging

from models.QuizSession import QuizSession
from models.User import User
from models.UserAnswer import UserAnswer
from models.MultipleChoice import MultipleChoiceQuestion

from repositories.QuizSessionRepository import QuizSessionRepository
from services.QuizGame import QuizGame

# Suprime mensagens de debug do watchdog/inotify (usado pelo Flask em modo debug)
logging.getLogger("watchdog.observers.inotify").setLevel(logging.WARNING)
logging.getLogger("watchdog").setLevel(logging.WARNING)

from flask import (
    Flask,
    render_template,
    request,
    session,
    redirect,
    url_for,
    jsonify,
)

from models.InvalidCredentialError import InvalidCredentialsError
from models.Quiz import Quiz

from repositories.QuizRepository import QuizRepository
from repositories.UserRepository import UserRepository
from repositories.UserAnswerRepository import UserAnswerRepository

from services.AuthService import AuthService
from .helpers import *

import json

app = Flask(__name__)  # initialize the class with name application.
app.secret_key = "my_local_secret_key"


@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Validando se os campos foram enviados
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password or not name:
            return return_error(
                "Error: name or email or password is not defined!!!", "/register"
            )

        try:
            auth = AuthService()
            session["user"] = (auth.register(name, email, password)).user_id

        except Exception as e:
            return return_error(f"Error: {e}", "/register")

        # Se o usuário for registrado com sucesso, redireciona para a página inicial.
        return redirect(url_for("index"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        # Validando se o email e senha foram enviado
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            return return_error("Error: email or password is not defined!!!", "/login")

        try:
            auth = AuthService()
            session["user"] = (auth.login(email, password)).user_id
        except InvalidCredentialsError:
            return return_error("Error: User is not defined!!!", "/login")

        # redirect do home
        return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    # Remove o usuário da sessão
    session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/quiz/create")
@login_required
def create_quiz():
    return render_template("create_quiz.html")


@app.route("/quiz/save", methods=["POST"])
def save_quiz():
    if request.method == "POST":
        try:
            quiz_info = Quiz.from_dict(request.get_json())

            quiz_repo = QuizRepository()
            quiz_repo.create(quiz_info)
        except Exception as e:
            print(f"Aconteceu um erro {e}")

        return jsonify({"info": "API funcionando"}), 200


# Catálogo de quizzes
@app.route("/quizzes")
@login_required
def quizzes_page():
    return render_template("quizzes_list.html")


@app.route("/api/quizzes")
def quizzes_api():
    quiz_repo = QuizRepository()
    list_quiz = quiz_repo.get_most_popular()  # retorna uma list[quiz]
    return [d.to_dict() for d in list_quiz]


@app.route("/api/quizzes/search")
@login_required
def get_quizzes():
    quiz_repo = QuizRepository()
    list_quiz = quiz_repo.get_by_category(request.args.get("category"))

    if not list_quiz:
        return []
    return [d.to_dict() for d in list_quiz]


@app.route("/quiz/<int:quiz_id>/play", methods=["GET", "POST"])
@login_required
def quiz_init(quiz_id):
    # Inicializa o quiz
    if request.method == "GET":

        # Pesistência da run
        session["quiz_session"] = {
            "session_id": 0,
            "user_id": session["user"],
            "quiz_id": int(quiz_id),
            "current_question": 0,
            "score": 0,
        }

        quiz_repo = QuizRepository()
        user_repo = UserRepository()

        quiz_game = QuizGame(
            quiz=quiz_repo.get_by_id(session["quiz_session"].get("quiz_id")),
            user=user_repo.get_by_id(session["user"]),
        )
        quiz_session = QuizSessionRepository()
        session["quiz_session"]["session_id"] = quiz_session.create(
            QuizSession.from_dict(session["quiz_session"])
        )

        question = quiz_game.start_game()  # -> MultipleChoiceQuestions

        # Retornando a primeira pergunta.
        return render_template("quiz_run.html", question=question.to_dict())

    # Registra respostas e mantém fluxo
    else:  # POST

        response = request.get_json()

        # Reinicializando o quiz

        quiz_repo = QuizRepository()
        user_repo = UserRepository()

        quiz_game = QuizGame(
            quiz=quiz_repo.get_by_id(session["quiz_session"].get("quiz_id")),
            user=user_repo.get_by_id(session["user"]),
            current_quesiton_index=session["quiz_session"]["current_question"],
        )

        #  Criar o objeto UserAnswer com os dados da resposta do usuário
        user_answer = UserAnswer(
            user_id=session["quiz_session"].get("user_id"),
            quiz_id=session["quiz_session"].get("quiz_id"),
            question_id=response.get("question_id"),
            selected_option=response.get("selected_option"),
            time_to_response=response.get("time_to_response"),
        )

        # Valida resposta, registra no banco e incrementa current_question e retorna se o quiz irá continuar ou não
        next_question = quiz_game.register_user_response(user_answer)

        # Incrementa o score na sessão.
        session["quiz_session"]["score"] += quiz_game.score

        if next_question:

            # Incrementar o contador de questão atual na sessão
            session["quiz_session"]["current_question"] += 1

            # Sincronizar a sessão atualizada com o banco quiz_sessions
            quiz_session = QuizSessionRepository()

            quiz_session.update_session(QuizSession.from_dict(session["quiz_session"]))

            return jsonify(next_question)
        else:
            # Sincronizar a sessão atualizada com o banco quiz_sessions
            quiz_session = QuizSessionRepository()
            quiz_session.update_session(QuizSession.from_dict(session["quiz_session"]))

            # Quiz game já atualizaou o QuizResult no banco marcando como completo
            return jsonify({"status": "completed"})


"""
Rotas faltantes:
    - Rota /quiz/<quiz_id>/result para ver resultado do quiz
    - Rota /statistics para visualizar estatísticas gerais
"""
