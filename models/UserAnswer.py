class UserAnswer:
    """
    Classe modelo para o encapsulamento do histórico de respostas do usuário.
    """

    def __init__(
        self,
        user_id: int = None,
        quiz_id: int = None,
        question_id: int = None,
        selected_option: int = None,
        is_correct: bool = None,
        time_to_response: float = 0,
    ):
        self.user_id = user_id
        self.quiz_id = quiz_id
        self.question_id = question_id
        self.selected_option = selected_option
        self.is_correct = is_correct
        self.time_to_response = time_to_response

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def quiz_id(self):
        return self._quiz_id

    @quiz_id.setter
    def quiz_id(self, quiz_id):
        self._quiz_id = quiz_id

    @property
    def question_id(self):
        return self._question_id

    @question_id.setter
    def question_id(self, question_id):
        self._question_id = question_id

    def __str__(self):
        return f"""
        User id: {self.user_id},\n
        Quiz id: {self.quiz_id},\n
        Question id: {self.question_id},\n
        Selected Option: {self.selected_option},\n
        Is correct: {self.is_correct},\n
        Time to response: {self.time_to_response}
        """
