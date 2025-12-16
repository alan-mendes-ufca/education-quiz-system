import logging

from models.QuizSession import QuizSession
from models.User import User
from models.UserAnswer import UserAnswer
from models.MultipleChoice import MultipleChoiceQuestion
from models.QuizResult import QuizResult

from services.QuizGame import QuizGame

# Suprime mensagens de debug do watchdog/inotify (usado pelo Flask em modo debug)
logging.getLogger("watchdog.observers.inotify").setLevel(logging.WARNING)
logging.getLogger("watchdog").setLevel(logging.WARNING)

import os
from dotenv import load_dotenv

load_dotenv(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
)  # Carrega variáveis de ambiente do arquivo .env, que está na raiz do projeto.
import os

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


from repositories.QuizSessionRepository import QuizSessionRepository
from repositories.QuizRepository import QuizRepository
from repositories.UserRepository import UserRepository
from repositories.QuestionRepository import QuestionRepository
from repositories.QuizResultRepository import QuizResultRepository

from services.AuthService import AuthService
from .helpers import *

app = Flask(__name__)  # initialize the class with name application.
app.secret_key = os.getenv("MY_SECRET_KEY")  # used to secure a session.


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

            # Salva as questões
            questions = quiz_info.questions  # list[MultipleChoiceQuestion]
            quest_repo = QuestionRepository()
            for question in questions:
                quest_repo.create(question)

        except Exception as e:
            print(f"Aconteceu um erro {e}")
            return jsonify({"info": "erro na API"}), 400
        return jsonify({"info": "API funcionando"}), 200

    return jsonify({"info": "método inválido"}), 405


# Catálogo de quizzes
@app.route("/quizzes")
@login_required
def quizzes_page():
    return render_template("quizzes_list.html")


@app.route("/api/quizzes")
def quizzes_api():

    if request.method != "GET":
        return jsonify({"info": "método inválido"}), 405

    quiz_repo = QuizRepository()
    list_quiz = quiz_repo.get_most_popular()  # retorna uma list[quiz]
    return [d.to_dict() for d in list_quiz]


@app.route("/api/quizzes/search")
def get_quizzes():
    if request.method != "GET":
        return jsonify({"info": "método inválido"}), 405

    category = request.args.get("category")
    if not category:
        return jsonify([]), 200

    quiz_repo = QuizRepository()
    list_quiz = quiz_repo.get_by_category(category)

    if not list_quiz:
        return jsonify([]), 200
    return jsonify([d.to_dict() for d in list_quiz]), 200


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
            "current_question_index": 0,
            "score": 0,
        }

        quiz_repo = QuizRepository()
        user_repo = UserRepository()

        quiz_game = QuizGame(
            quiz=quiz_repo.get_by_id(session["quiz_session"].get("quiz_id")),
            user=user_repo.get_by_id(session["user"]),
        )

        session_repo = QuizSessionRepository()

        session_data = session["quiz_session"]

        # Persistindo a sessão no banco de dados e retornando o id criado.
        session_data["session_id"] = session_repo.create(
            QuizSession.from_dict(session_data)
        )
        session["quiz_session"] = (
            session_data  # <-Reatribui, confirmando a alteração da session.
        )

        question = quiz_game.start_game()  # -> MultipleChoiceQuestions
        # Retornando a primeira pergunta.
        return render_template("quiz_run.html", question=question.to_dict())

    # Registra respostas e mantém fluxo
    else:  # POST

        response = request.get_json().get("question")

        # Pega o dict da sessão
        session_data = session["quiz_session"]

        # Reinicializando o quiz

        quiz_repo = QuizRepository()
        user_repo = UserRepository()

        quiz_game = QuizGame(
            quiz=quiz_repo.get_by_id(session_data.get("quiz_id")),
            user=user_repo.get_by_id(session["user"]),
            current_question_index=session_data.get("current_question_index"),
            session_id=session_data.get("session_id"),
        )

        #  Criar o objeto UserAnswer com os dados da resposta do usuário
        user_answer = UserAnswer(
            user_id=session_data.get("user_id"),
            quiz_id=session_data.get("quiz_id"),
            question_id=response.get("id"),
            selected_option=response.get("selected_alternative"),
            time_to_response=response.get("time_to_response", 0),
        )

        # Valida resposta, registra no banco e incrementa current_question_index e retorna se o quiz irá continuar ou não
        next_question = quiz_game.register_user_response(user_answer)

        # Incrementa o score na sessão.
        session_data["score"] += quiz_game.score

        if next_question:

            # Incrementar o contador de questão atual na sessão
            session_data["current_question_index"] += 1

            # Reatribui para session
            session["quiz_session"] = session_data

            # Sincronizar a sessão atualizada com o banco
            quiz_session = QuizSessionRepository()
            quiz_session.update_session(QuizSession.from_dict(session_data))

            return jsonify(
                {
                    "question": next_question.to_dict(),
                    "status": True,
                    "session_id": session_data.get("session_id"),
                }
            )
        else:
            # Salvar resultado do quiz
            quiz_game.finish_game(
                {
                    "user": quiz_game.user,
                    "quiz": quiz_game.quiz,
                    "quiz_session": quiz_game.session_id,
                    "score_achieved": session_data.get("score"),
                    "time_taken": quiz_game.get_total_time(),
                    "max_possible_score": quiz_game.quiz.get_max_score(),
                }
            )
            # Sincronizar a sessão atualizada com o banco quiz_sessions
            quiz_session = QuizSessionRepository()
            quiz_session.update_session(QuizSession.from_dict(session_data))

            # Quiz game já atualizaou o QuizResult no banco marcando como completo
            return jsonify(
                {"status": False, "session_id": session_data.get("session_id")}
            )


@app.route("/quiz/<int:session_id>/result")
def result(session_id):
    result_repo = QuizResultRepository()
    data = result_repo.get_results_by_session(session_id)

    if not data:
        return return_error("Resultado não encontrado", "/quizzes")

    """
    `**` é um operador de desempacotamento de dicionários.
    Ele pega cada par chave-valor do dicionário `data` e os passa como argumentos nomeados.
    
    return render_template("result.html", 
    user=data["user"], 
    quiz=data["quiz"], 
    score=data["score"], 
    time=data["time"])
    
    """
    return render_template("result.html", **data)


"""
Rotas faltantes:
    - Rota /statistics para visualizar estatísticas gerais
"""
