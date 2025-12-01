import os
from cs50 import SQL
from models.User import User
from models.InvalidCredentialError import InvalidCredentialsError


class UserRepository:
    """
    Responsável pela persistência(CRUD) dos usuários cadastrados.
    - Métodos: create(user: User), get_by_id(user_id) -> User, get_by_email(email) -> User, update(user: User).
    - Relacionamento/descrição: "Empacota" os dados de uma consulta de usuários em um objeto User. Em outros contexto também criará uma linha na tabela de usuários por meio de um objeto User fornecido pelo AuthService.

    """

    def __init__(self, db_url=None):
        # Corrige o caminho para o banco de dados
        if db_url is None:
            db_path = os.path.join(
                os.path.dirname(os.path.dirname(__file__)), "data", "app.db"
            )
            db_url = f"sqlite:///{db_path}"
        self.db = SQL(db_url)

    def create(self, user: User) -> User:
        """
        Valida a existência de um usuário no banco de dados, se o registro estiver disponível os dados são inseridos para persistência.
        """
        alredy_exist = self.db.execute("SELECT * FROM user WHERE email = ?", user.email)

        if alredy_exist:
            raise InvalidCredentialsError("User already exists.")

        try:
            self.db.execute(
                "INSERT INTO user (name, email, password_hash) VALUES (?, ?, ?)",
                user.name,
                user.email,
                user.password_hash,
            )
        except ValueError:
            raise InvalidCredentialsError(
                "User already exists."
            )  # Se já existir um usuário cadastrado com essa informações, ele retornará um erro.

        return self.get_by_email(user.email)

    def get_by_id(self, user_id) -> User:
        """
        Busca um usuário pelo id.
        """
        # Select retorna uma lista de dicionários. É preciso validar se a lista é vazia ou não.
        # Se a lista não for vazia, ele retornará o primeiro elemento da lista `rows[0]`.
        rows = self.db.execute("SELECT * FROM user WHERE id = ?", user_id)
        if not rows:
            return None
        return User.constructor_dict(rows[0])

    def get_by_email(self, email) -> User:
        """
        Busca um usuário pelo email.
        """
        rows = self.db.execute("SELECT * FROM user WHERE email = ?", email)
        if not rows:
            return None
        return User.constructor_dict(rows[0])

    def update(self, user: User) -> User:
        """
        Altera dados cadastrais de um usuário.
        """
        self.db.execute(
            "UPDATE user SET name = ?, email = ?, password_hash = ? WHERE id = ?",
            user.name,
            user.email,
            user.password_hash,
            user.user_id,
        )
        return self.get_by_id(user.user_id)
