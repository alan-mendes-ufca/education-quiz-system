from crypt import methods
import logging
from unicodedata import category

from models.QuizSession import QuizSession
from models.User import User
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
    flash,
    redirect,
    url_for,
    jsonify,
)

from models.InvalidCredentialError import InvalidCredentialsError
from models.Quiz import Quiz

from repositories.QuizRepository import QuizRepository
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
        return redirect("/")

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
        return redirect("/")

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    # Remove o usuário da sessão
    session.pop("user", None)
    return redirect("/login")


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
def quizzes_page():
    return render_template("quizzes_list.html")


@app.route("/api/quizzes")
def quizzes_api():
    quiz_repo = QuizRepository()
    list_quiz = quiz_repo.get_most_popular()  # retorna uma list[quiz]
    return [d.to_dict() for d in list_quiz]


@app.route("/api/quizzes/search")
def get_quizzes():
    quiz_repo = QuizRepository()
    list_quiz = quiz_repo.get_by_category(request.args.get("category"))

    if not list_quiz:
        return []
    return [d.to_dict() for d in list_quiz]


@app.route("/quiz/<int:quiz_id>/play", methods=["GET", "POST"])
def quiz_init(quiz_id):
    # Inicializa o quiz
    if request.method == "GET":
        quiz_repo = QuizRepository
        q_game = QuizGame(quiz_repo.get_by_id(quiz_id), session["user"])

        # Pesistência da run
        session["quiz_session"] = {
            "user_id": session["user"],
            "quiz_id": quiz_id,
            "current_question": 0,
            "score": 0,
        }

        quiz_session = QuizSessionRepository()
        quiz_session.create(QuizSession.from_dict(session["quiz_session"]))

        # Retornando a primeira pergunta.
        return render_template("quiz_run.html", question=q_game.start_game())

    # Registra respostas e mantém fluxo
    else:
        # Persistência da resposta do usuário com UserAnswers
        # Atualizar sessão
        # Retornar próxima questão para o front
        pass


"""
Rotas faltantes:
    - Rota /quiz/<quiz_id>/result para ver resultado do quiz
    - Rota /statistics para visualizar estatísticas gerais
    - Rota /statistics/user para estatísticas do usuário logado
    - Rota /question/create (GET/POST) para criar novas questões
"""
