from models.User import User
from models.Quiz import Quiz
from models.QuizSession import QuizSession


class QuizResult:
    """
    Define as características básicas e CONFIGURAÇÕES do quiz.
    """

    def __init__(
        self,
        user: User,
        quiz: Quiz,
        quiz_session: QuizSession,
        score_achieved: int,
        time_taken: float,
        max_possible_score: int,
    ):
        self.user = user
        self.quiz = quiz
        self.quiz_session = quiz_session
        self.score_achieved = score_achieved
        self.time_taken = time_taken
        self.max_possible_score = max_possible_score

    def __str__(self):
        return f"""
        User id: {self.user.user_id},\n
        Quiz id: {self.quiz.quiz_id},\n
        Score: {self.score_achieved},\n
        Time: {self.time_taken},\n
        Max possible score: {self.max_possible_score}
        """
