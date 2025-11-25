class UserAnswer:
    """
    Classe modelo para o encapsulamento do histórico de respostas do usuário.
    """

    def __init__(
        self, id: int, quiz_result_id: int, question_id: int, is_correct: bool
    ):
        self.id = id
        self.quiz_result_id = quiz_result_id
        self.question_id = question_id
        self.is_correct = is_correct

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

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

    @property
    def is_correct(self):
        return self._is_correct

    @is_correct.setter
    def is_correct(self, is_correct):
        self._is_correct = is_correct
