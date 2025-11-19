from .User import User
from .Quiz import Quiz

class Quiz_result():
    """
        Define as características básicas e CONFIGURAÇÕES do quiz.
    """
    def __init__(self, user:User, quiz: Quiz, score_achieved: int, time_taken: float, responses_history:dict):
        self.user = user
        self.quiz = quiz
        self.score = score_achieved
        self.time = time_taken
        self.responses = responses_history