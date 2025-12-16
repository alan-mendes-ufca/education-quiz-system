class QuizSession:
    """
    Classe modelo para a persistência da sessão do quiz.
    """

    def __init__(
        self,
        session_id: int = None,
        user_id: int = None,
        quiz_id: int = None,
        current_question_index: int = None,
        score: int = None,
    ):
        self.session_id = session_id
        self.user_id = user_id
        self.quiz_id = quiz_id
        self.current_question_index = current_question_index
        self.score = score

    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        self._session_id = session_id

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, id):
        self._user_id = id

    @property
    def quiz_id(self):
        return self._quiz_id

    @quiz_id.setter
    def quiz_id(self, id):
        self._quiz_id = id

    @property
    def current_question_index(self):
        return self._current_question_index

    @current_question_index.setter
    def current_question_index(self, question):
        self._current_question_index = question

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, s):
        self._score = s

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            session_id=d.get("session_id", None),
            user_id=d.get("user_id"),
            quiz_id=d.get("quiz_id"),
            current_question_index=d.get("current_question_index"),
            score=d.get("score"),
        )

    def __str__(self):
        return f"QuizSession(session_id={self.session_id}, user_id={self.user_id}, quiz_id={self.quiz_id}, current_question_index={self.current_question_index}, score={self.score})"
