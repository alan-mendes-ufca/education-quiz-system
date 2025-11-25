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
        responses_history: str,
    ):
        self.user = user
        self.quiz = quiz
        self.score_achieved = score_achieved
        self.time_taken = time_taken
        self.responses_history = responses_history
