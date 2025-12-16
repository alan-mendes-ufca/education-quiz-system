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

    def save(self, us_answer: UserAnswer) -> int:
        """
        Salva a resposta do usuário no banco de dados.
        """
        try:
            user_answer_id = self.db.execute(
                "INSERT INTO user_answer (user_id, quiz_id, question_id, selected_option, is_correct,time_to_response) VALUES (?, ?, ?, ?, ?, ?);",
                us_answer.user_id,
                us_answer.quiz_id,
                us_answer.question_id,
                us_answer.selected_option,
                "t" if us_answer.is_correct is True else "f",
                us_answer.time_to_response,
            )
        except Exception as e:
            raise ValueError("Erro ao salvar a resposta do usuário: " + str(e))
        return user_answer_id

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
        result = self.db.execute(
            """
            SELECT ua.question_id, mcq.proposition, COUNT(*) AS miss_count
            FROM user_answer ua
            JOIN multiple_choice_question mcq ON ua.question_id = mcq.id
            WHERE ua.is_correct = 'f'
            GROUP BY ua.question_id, mcq.proposition
            ORDER BY miss_count DESC
            LIMIT 1;
            """
        )
        if not result:
            return None
        return {
            "question_id": result[0]["question_id"],
            "proposition": result[0]["proposition"],
            "miss_count": result[0]["miss_count"],
        }

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
        result = self.db.execute(
            """
            SELECT ua.question_id, mcq.proposition, COUNT(*) AS count_correct
            FROM user_answer ua
            JOIN multiple_choice_question mcq ON ua.question_id = mcq.id
            WHERE ua.is_correct = 't'
            GROUP BY ua.question_id, mcq.proposition
            ORDER BY count_correct DESC
            LIMIT 1;
            """
        )
        if not result:
            return None
        return {
            "question_id": result[0]["question_id"],
            "proposition": result[0]["proposition"],
            "count_correct": result[0]["count_correct"],
        }
