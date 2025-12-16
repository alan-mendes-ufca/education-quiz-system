import os
from cs50 import SQL
from models.QuizSession import QuizSession


class QuizSessionRepository:
    """
    Responsável pelo percistẽncia(CRUD) da sessão.
    """

    def __init__(self, db_url=None):
        # Corrige o caminho para o banco de dados
        if db_url is None:
            db_path = os.path.join(
                os.path.dirname(os.path.dirname(__file__)), "data", "app.db"
            )
            db_url = f"sqlite:///{db_path}"
        self.db = SQL(db_url)

    def create(self, session: QuizSession) -> int:
        """
        Adiciona as informações sobre o quiz no repositório.
        """

        try:
            session_id = self.db.execute(
                "INSERT INTO quiz_session (quiz_id, user_id, current_question_index, score) VALUES (?, ?, ?, ?)",
                session.quiz_id,
                session.user_id,
                session.current_question_index,
                session.score,
            )
        except Exception as e:
            raise ValueError(f"Não foi possível salvar o quiz, aconteceu um erro: {e}")

        return session_id

    def get_by_id(self, user_id, quiz_id):
        """
        Seleciona um quiz pelo id dele.
        """
        rows = self.db.execute(
            "SELECT * FROM quiz_session WHERE user_id = ? AND quiz_id = ?",
            user_id,
            quiz_id,
        )

        if not rows:
            raise ValueError("Nenhum quiz tribuído ao id fornecido.")

        return QuizSession.from_dict(rows[0])

    def update_session(
        self,
        session: QuizSession,
    ) -> int:

        try:
            self.db.execute(
                "UPDATE quiz_session SET current_question_index = ?, score = ? WHERE id = ?;",
                session.current_question_index,
                session.score,
                session.session_id,
            )
        except Exception as e:
            raise ValueError(
                f"Não foi possível atualizar a sessão, aconteceu um erro: {e}"
            )
