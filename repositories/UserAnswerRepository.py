from cs50 import SQL

"""
Responsável pela persistências das respostas do usuário.
- atributos: db = SQL(db_url)
- métodos: get_most_missed_question, get_most_correct_question
"""


class UserAnswerRepository:
    def __init__(self, db_url=r"sqlite:///../data/app.db"):
        self.db = SQL(db_url)

    def get_most_missed_question_by_quiz(self, quiz_id):
        """
        Retorna a questão que mais erraram em um quiz específico.
        """
        pass

    def get_most_missed_question_all(self):
        """
        Retorna a questão que mais erraram dentre todos os quizzes.
        """
        pass

    def get_most_correct_question_by_quiz(self, quiz_id):
        """
        Retorna a questão que mais acertada em um quiz específico.
        """
        pass

    def get_most_correct_question_all(self):
        """
        Retorna a questão que mais acertada dentre todos os quizzes.
        """
        pass
