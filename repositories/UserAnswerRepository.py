import os
from cs50 import SQL
from models.UserAnswer import UserAnswer

"""
Responsável pela persistências das respostas do usuário.
- atributos: db = SQL(db_url)
- métodos: get_most_missed_question, get_most_correct_question
"""


class UserAnswerRepository:
    def __init__(self, db_url=None):
        # Corrige o caminho para o banco de dados
        if db_url is None:
            db_path = os.path.join(
                os.path.dirname(os.path.dirname(__file__)), "data", "app.db"
            )
            db_url = f"sqlite:///{db_path}"
        self.db = SQL(db_url)

    def save(self, us_answer: UserAnswer):
        self.db.execute(
            "INSERT INTO user_answer (user_id, quiz_result_id, question_id, selected_option, is_correct) VALUES (?, ?, ?, ?, ?);",
            us_answer.user_id,
            us_answer.quiz_id,
            us_answer.question_id,
            us_answer.selected_option,
            "t" if us_answer.is_correct is True else "f",
        )

    def get_most_missed_question_by_quiz(self, quiz_id):
        """
        Retorna as questões mais erradas em um quiz específico.
        """
        return self.db.execute(
            """
            SELECT question_id, COUNT(*) AS miss_count
            FROM user_answer
            WHERE is_correct = 'f' AND quiz_id = ?
            GROUP BY question_id
            ORDER BY miss_count DESC
            LIMIT 1;
            """,
            quiz_id,
        )

    def get_most_missed_question_all(self):
        """
        Retorna a questão que mais erraram dentre todos os quizzes.
        """
        return self.db.execute(
            """
            SELECT question_id, COUNT(*) AS miss_count
            FROM user_answer
            WHERE is_correct = 'f'
            GROUP BY question_id
            ORDER BY miss_count DESC
            LIMIT 1;
            """
        )

    def get_most_correct_question_by_quiz(self, quiz_id):
        """
        Retorna a questão que mais acertada em um quiz específico.
        """
        return self.db.execute(
            """
            SELECT question_id, COUNT(*) AS count_correct
            FROM user_answer
            WHERE is_correct = 't' AND quiz_id = ?
            GROUP BY question_id
            ORDER BY count_correct DESC
            LIMIT 1;
            """,
            quiz_id,
        )

    def get_most_correct_question_all(self):
        """
        Retorna a questão que mais acertada dentre todos os quizzes.
        """
        return self.db.execute(
            """
            SELECT question_id, COUNT(*) AS count_correct
            FROM user_answer
            WHERE is_correct = 't'
            GROUP BY question_id
            ORDER BY count_correct DESC
            LIMIT 1;
            """
        )
