from .User import User
from .Quiz import Quiz


class QuizResult:
    """
    Define as características básicas e CONFIGURAÇÕES do quiz.
    """

    def __init__(
        self,
        user: User,
        quiz: Quiz,
        score_achieved: int,
        time_taken: float,
        max_possible_score: int,
    ):
        self.user = user
        self.quiz = quiz
        self.score_achieved = score_achieved
        self.time_taken = time_taken
        self.max_possible_score = max_possible_score
