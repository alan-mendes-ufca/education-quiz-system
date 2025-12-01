import Question


class MultipleChoiceQuestion(Question):
    """
    Responsável por guardar os dados das questões de multipla escolha.
    """

    def __init__(
        self,
        question_id: int = None,
        proposition: str = None,
        theme: str = None,
        difficulty_points: int = None,
        options: list = None,
        correct_option_index: int = None,
    ):
        super().__init__(question_id, proposition, theme, difficulty_points)
        self.options = options
        self.correct_option_index = correct_option_index

    def check_answer(self, user_answer_index):
        """
        Verifica se a resposata é válida.
        """
        if user_answer_index != self.correct_option_index:
            return 0
        return self.difficulty_points

    @classmethod
    def constructor_dict(cls, dict):
        """
        Retorna uma instância da classe, sendo sua contrução abnstraída de um dicionário.
        """
        return cls(
            dict["id"],
            dict["proposition"],
            dict["theme"],
            dict["difficulty_points"],
            dict["options"],
            dict["correct_option_index"],
        )
