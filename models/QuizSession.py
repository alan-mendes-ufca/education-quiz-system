class QuizSession :
    """
    Classe modelo para a persistência da sessão do quiz.
    """
    def __init__(self, user_id : int = None, quiz_id : int = None, current_question : int = None, score:int = None):
        self.user_id = user_id
        self.quiz_id = quiz_id
        self.current_question = current_question
        self.score = score
    
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
    def current_question(self):
        return self._current_question
    
    @current_question.setter
    def current_question(self, question):
        self._current_question = question
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, s):
        self._score = s

    @classmethod
    def from_dict(cls, d : dict):
        return cls(
            user_id = d.get("user_id"),
            quiz_id = d.get("quiz_id"),
            current_questions = d.get("current_quesion"),
            score = d.get("score")
        )