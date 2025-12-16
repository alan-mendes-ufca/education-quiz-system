from models.Question import Question


class MultipleChoiceQuestion(Question):
    """
    Classe responsável por guardar os dados de questões de múltipla escolha.
    """

    def __init__(
        self,
        question_id: int = None,
        proposition: str = None,
        category: str = None,
        difficulty_points: int = None,
        alternatives: list = None,
        correct_option_index: int = None,
    ):
        super().__init__(question_id, proposition, category, difficulty_points)
        self.alternatives = alternatives if alternatives is not None else []
        self.correct_option_index = correct_option_index

    @property
    def correct_option_index(self) -> int:
        return self._correct_option_index

    @correct_option_index.setter
    def correct_option_index(self, value: int):
        if not isinstance(value, int) or not (0 <= value < len(self.alternatives)):
            raise ValueError("Índice da opção correta inválido.")
        self._correct_option_index = value

    def check_answer(self, user_answer_index: int) -> int:
        """
        Verifica se a resposta do usuário está correta.
        Retorna os pontos da questão se correto, 0 se incorreto.
        """
        if not 0 <= user_answer_index < len(self.alternatives):
            raise ValueError("Índice da resposta inválido.")
        return (
            {"score": self.difficulty_points, "is_correct": True}
            if user_answer_index == self.correct_option_index
            else {"score": 0, "is_correct": False}
        )

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria uma instância da classe a partir de um dicionário.
        """

        return cls(
            question_id=data.get("id"),
            proposition=data.get("proposition"),
            category=data.get("category"),
            difficulty_points=data.get("difficulty_points"),
            alternatives=data.get("alternatives", []),
            correct_option_index=data.get("correct_option_index"),
        )

    def to_dict_public(self):
        """
        Retorna um dicionário com os dados públicos da questão (sem a resposta correta).
        """
        return {
            "id": self.question_id,
            "proposition": self.proposition,
            "category": self.category,
            "difficulty_points": self.difficulty_points,
            "alternatives": self.alternatives,
        }

    def to_dict(self):
        """
        Retorna um dicionário com todos os dados da questão (incluindo a resposta correta).
        """
        return {
            "id": self.question_id,
            "proposition": self.proposition,
            "category": self.category,
            "difficulty_points": self.difficulty_points,
            "alternatives": self.alternatives,
            "correct_option_index": self.correct_option_index,
        }

    def __str__(self):
        alternatives_str = "\n".join(
            f"{i}. {opt}" for i, opt in enumerate(self.alternatives)
        )
        return (
            f"Question ID: {self.question_id}\n"
            f"Title: {self.proposition}\n"
            f"category: {self.category}\n"
            f"Difficulty Points: {self.difficulty_points}\n"
            f"alternatives:\n{alternatives_str}\n"
            f"Correct Option Index: {self.correct_option_index}"
        )
