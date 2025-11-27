class UserAnswer:
    """
    Classe modelo para o encapsulamento do histórico de respostas do usuário.
    """

    def __init__(
        self,
        user_id: int = None,
        quiz_result_id: int = None,
        question_id: int = None,
        selected_option: int = None,
        is_correct: bool = None,
    ):
        self.user_id = user_id
        self.quiz_result_id = quiz_result_id
        self.question_id = question_id
        self.selected_option = selected_option
        self.is_correct = is_correct

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def quiz_result_id(self):
        return self._quiz_id

    @quiz_result_id.setter
    def quiz_result_id(self, quiz_result_id):
        self._quiz_id = quiz_result_id

    @property
    def question_id(self):
        return self._question_id

    @question_id.setter
    def question_id(self, question_id):
        self._question_id = question_id
