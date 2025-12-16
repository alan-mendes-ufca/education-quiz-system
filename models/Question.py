from abc import ABC, abstractmethod


class Question(ABC):
    """
    Responsável por definir os atributos mínimos para diferentes modelos de questões.
    - Método: check_answer(user_answer): método abstrato, define uma responsabilidade para as classes
    filhas. A implementação futura nas outras classes será forçada, o que pode ser feito de duas formas:
    - dentro do método atual terá :raise NotImplementedError("A subclasse esqueceu de implementar este método!").
    - *maneira mais elegante e correta*: utilizando o decorador @abstractmethod que, mesmo se os métodos das subclasses estejam totalmente funcionais,
    retornará ume erro pois check_answer não foi implementado.
    """

    def __init__(
        self,
        question_id: int = None,
        proposition: str = None,
        category: str = None,
        difficulty_points: int = None,
    ):
        self.question_id = question_id
        self.proposition = proposition
        self.category = category
        self.difficulty_points = difficulty_points

    @property
    def question_id(self):
        return self.__question_id

    @question_id.setter
    def question_id(self, question_id):
        self.__question_id = question_id

    @abstractmethod
    def check_answer(self, user_answer):
        """
        Método abstrado que deixa uma dívida para as classes filhas.
        """
        pass
