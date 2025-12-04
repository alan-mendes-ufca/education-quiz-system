from functools import wraps
from flask import session, flash, redirect


def return_error(message, page):
    flash(message, category='danger') # Informa ao usuário o erro ocorrido.
    return redirect(page) # Redireciona o usuário para a página especificada.


def login_required(f):
    """
    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function
