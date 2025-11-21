from cs50 import SQL
from models.InvalidCredentialError import InvalidCredentialsError
from models.User import User
from repositories.UserRepository import UserRepository
from services.AuthService import AuthService
import pytest

db_url="sqlite:///test_data/test_db.sqlite3"

def db_resete():
    db = SQL(db_url)
    db.execute("DROP TABLE IF EXISTS user;")
    db.execute("CREATE TABLE user ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, password_hash TEXT NOT NULL UNIQUE);")

def test_register():
    db_resete()
    # Instaciando a classe AuthService e passando o db_url como o `test_app.db`
    auth = AuthService(user_repository=UserRepository(db_url=db_url))
    # Registrando a primeira vez: nenhum erro esperado.
    result = auth.register("teste", "teste@gmail.com", "teste12345")
    assert isinstance(result, User)

    # Ao tentar registrar o mesmo usuário novamente um erro deve ser retornado.
    with pytest.raises(InvalidCredentialsError, match="User already exists."):
        auth.register("teste", "teste@gmail.com", "teste12345")
