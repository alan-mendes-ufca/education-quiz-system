from flask import Flask, render_template, request, session

from models.InvalidCredentialError import InvalidCredentialsError
from services.AuthService import AuthService
from .helpers import *

app = Flask(__name__)  # initialize the class with name application.
app.secret_key = "my_local_secret_key"


@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        # Validando se o email e senha foram enviado
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            return_error("Error: email or password is not defined!!!", "login.html")

        try:
            auth = AuthService()
            session["user"] = (auth.login(email, password)).user_id
        except InvalidCredentialsError:
            return_error("Error: User is not defined!!!", "/login")

        # redirect do home
        return redirect("/")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Validando se o email e senha foram enviado
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password or not name:
            return_error(
                "Error: name or email or password is not defined!!!", "/register"
            )

        try:
            auth = AuthService()
            session["user"] = (auth.login(email, password)).user_id
        except InvalidCredentialsError:
            return_error("Error: User already exist!!!", "/login")

        # redirect to index
        return redirect("/")

    return render_template("register.html")
