from models.Question import Question


class MultipleChoiceQuestion(Question):
    """
    Classe responsável por guardar os dados de questões de múltipla escolha.
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
        self.options = options if options is not None else []
        self.correct_option_index = correct_option_index

    def check_answer(self, user_answer_index: int) -> int:
        """
        Verifica se a resposta do usuário está correta.
        Retorna os pontos da questão se correto, 0 se incorreto.
        """
        if not 0 <= user_answer_index < len(self.options):
            raise ValueError("Índice da resposta inválido.")
        return (
            self.difficulty_points
            if user_answer_index == self.correct_option_index
            else 0
        )

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria uma instância da classe a partir de um dicionário.
        """
        return cls(
            question_id=data.get("id"),
            proposition=data.get("proposition"),
            theme=data.get("theme"),
            difficulty_points=data.get("difficulty_points"),
            options=data.get("options", []),
            correct_option_index=data.get("correct_option_index"),
        )

    def __str__(self):
        options_str = "\n".join(f"{i}. {opt}" for i, opt in enumerate(self.options))
        return (
            f"Question ID: {self.question_id}\n"
            f"Title: {self.proposition}\n"
            f"Theme: {self.theme}\n"
            f"Difficulty Points: {self.difficulty_points}\n"
            f"Options:\n{options_str}\n"
            f"Correct Option Index: {self.correct_option_index}"
        )
