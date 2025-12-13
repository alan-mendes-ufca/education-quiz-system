from models.MultipleChoice import MultipleChoiceQuestion
from models.Quiz import Quiz
from cs50 import SQL
import os
import json


class QuizRepository:
    """
    Responsável pelo percistẽncia(CRUD) dos quizzes.
    """

    def __init__(self, db_url=None):
        # Corrige o caminho para o banco de dados
        if db_url is None:
            db_path = os.path.join(
                os.path.dirname(os.path.dirname(__file__)), "data", "app.db"
            )
            db_url = f"sqlite:///{db_path}"
        self.db = SQL(db_url)

    def create(self, quiz: Quiz):
        """
        Adiciona as informações sobre o quiz no repositório.
        """

        try:
            self.db.execute(
                "INSERT INTO quiz (title, category , description, questions) VALUES (?, ?, ?, ?)",
                quiz.title,
                quiz.category,
                quiz.description,
                json.dumps([q.to_dict() for q in quiz.questions]),
            )
        except Exception as e:
            raise ValueError(f"Não foi possível salvar o quiz, aconteceu um erro: {e}")

    def get_by_id(self, id) -> Quiz:
        """
        Seleciona um quiz pelo id dele.
        """
        rows = self.db.execute("SELECT * FROM quiz WHERE id = ?", id)
        if not rows:
            raise ValueError("Nenhum quiz tribuído ao id fornecido.")

        return Quiz.from_dict(rows[0])

    def get_by_title(self, title) -> Quiz:
        """
        Seleciona um quiz pelo título específicado.
        """
        rows = self.db.execute("SELECT * FROM quiz WHERE title = ?", title)
        if not rows:
            return None
        return Quiz.from_dict(rows[0])

    def get_by_category(self, category) -> list[Quiz]:
        """
        Seleciona os quizzes por uma categoria específicado.
        """
        rows = self.db.execute("SELECT * FROM quiz WHERE category = ?", category)
        if not rows:
            return None
        return [Quiz.from_dict(row) for row in rows]

    def get_all(self) -> list[Quiz]:
        rows = self.db.execute("SELECT * FROM quiz;")
        if not rows:
            return None
        return [Quiz.from_dict(row) for row in rows]

    def get_most_popular(self) -> list[Quiz]:
        """
        Retorna os quizzes mais populares.
        - Ainda preciso implementar um log para definir a popularidade de um quiz;
        """
        rows = self.db.execute("SELECT * FROM quiz ORDER BY popularity LIMIT 10;")
        if not rows:
            return None
        return [Quiz.from_dict(row) for row in rows]
