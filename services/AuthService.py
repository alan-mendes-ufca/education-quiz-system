from models.User import User
from models.InvalidCredentialError import InvalidCredentialsError
from repositories.UserRepository import UserRepository
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session

class AuthService:
    """
    Controla as regras de negócio no que se diz respeito a autenticação(login, registro de usuário e logout).
    - Métodos: login(email, password) -> User, register(name, email, password) -> User, logout().
    - Relacionamento/descrição: Controla as regras de negócio no que se diz respeito a autenticação(login, registro de usuário e logout).
    """
    def __init__(self, user_repository = UserRepository):
        self.user_repository = user_repository
    
    def register(self, name: str, email: str, password: str) -> User:
        return self.user_repository.create(User(name=name, email=email, password_hash=generate_password_hash(password)))

    def login(cls, email: str, password: str) -> User:

        # Buscar login no banco de dados
        user = cls.user_repository.get_by_email(email)

        # check password_hash
        if not user or not check_password_hash(user.password_hash, password):
            return InvalidCredentialsError("Invalid email or password.")

        session["user_id"] = user.user_id

        return user

    @staticmethod
    def logout():
        session.clear()

