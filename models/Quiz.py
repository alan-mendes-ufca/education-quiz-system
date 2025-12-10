from unicodedata import category

from models.MultipleChoice import MultipleChoiceQuestion
from .Question import Question

import json

class Quiz:
    """
    Responsável por guardar os dados do quiz.
    - Por que recebe list[Question] sendo que as perguntas do quiz serão apenas de múltipla escolha(MultipleChoice)?
    Basicamente, MultipleChoice é uma classe filha de Question, ou seja ela também é uma question. Também abre flexibilidade para
    a utilização de outros tipos de pergunta como verdadeira ou falsa e por extenso.
    """

    def __init__(
        self, quiz_id: int = None, title: str = None, category : str = None, description : str = None, questions: list[Question] = None
    ):
        self.quiz_id = quiz_id
        self.title = title
        self.category = category
        self.description = description
        self.questions = questions

    @property
    def quiz_id(self):
        return self.__quiz_id

    @quiz_id.setter
    def quiz_id(self, quiz_id):
        self.__quiz_id = quiz_id

    @property
    def questions(self):
        # retorna um objeto imutável para impedir alterações na lista original por
        # classes externas (como QuizGame).
        return tuple(self._questions)

    @questions.setter
    def questions(self, questions):
        self._questions = questions

    def get_max_score(self):
        """
        Nota máxima possível acertanto todas as perguntas do quiz.
        - REGRA DE NEGÓCIO: A pontuação total é a soma dos pesos das perguntas.
        """

        score = 0
        for question in self.questions:
            score += question.difficulty_points

        return score

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            quiz_id=d.get("id"),
            title=d.get("title"), 
            category=d.get("category"), 
            description=d.get("description"), 
            questions = [MultipleChoiceQuestion.from_dict(question) for question in json.loads(d.get("questions"))]
        )

    def to_dict(self):
        return {
            "quiz_id": self.quiz_id,
            "title": self.title,
            "category": self.category,
            "description": self.description,
            "questions": [question.to_dict() for question in self.questions]
        }
    
    # Retorna dados básicos sobre o quiz.
    def __str__(self):
        questions_str = "\n".join(f"  - {str(question)}" for question in self.questions)
        return (
            f"quiz_id: {self.quiz_id}\n"
            f"Title: {self.title}\n"
            f"Category: {self.category}\n"
            f"Description: {self.description}\n"
            f"Questions:\n{questions_str}"
        )

    # Retorna o tamanho da lista de questões.
    def __len__(self):
        return len(self.questions)

    # Quando o objeto for colocado dentro de uma iteração ele retornará automaticamente a lista de questões.
    def __iter__(self):
        return iter(self.questions)