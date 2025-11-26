from cs50 import SQL
from models.InvalidCredentialError import InvalidCredentialsError
from models.User import User
from repositories.UserRepository import UserRepository
from services.AuthService import AuthService
import pytest

db_url = "sqlite:///" + r"db/test_auth_db.sqlite"


def db_reset():
    db = SQL(db_url)
    db.execute("DROP TABLE IF EXISTS user;")
    db.execute(
        "CREATE TABLE user ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, password_hash TEXT NOT NULL UNIQUE);"
    )


def test_register():
    db_reset()
    user_repo = UserRepository(db_url=db_url)

    # Instaciando a classe AuthService e passando o db_url como o `test_app.db`
    auth = AuthService(user_repository=user_repo)

    # Registrando a primeira vez: nenhum erro esperado.
    result = auth.register("teste", "teste@gmail.com", "teste12345")
    assert isinstance(result, User)
    assert result.name == "teste"
    assert result.email == "teste@gmail.com"

    # Verificando se o usuário foi inserido no bando de dados
    user_in_db = user_repo.get_by_email("teste@gmail.com")
    assert user_in_db.name == "teste"

    # Ao tentar registrar o mesmo usuário novamente um erro deve ser retornado.
    with pytest.raises(InvalidCredentialsError, match="User already exists."):
        auth.register("teste", "teste@gmail.com", "teste12345")
