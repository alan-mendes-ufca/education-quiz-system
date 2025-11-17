class Question:
    """
        Responsável por definir os atributos mínimos para diferentes modelos de questões.
        - Método: check_answer(user_answer): método abstrato, define uma responsabilidade para as classes
        filhas. A implementação futura nas outras classes será forçada, o que pode ser feito de duas formas: 
        - dentro do método atual terá :raise NotImplementedError("A subclasse esqueceu de implementar este método!"). 
        - *maneira mais elegante e correta*: utilizando o decorador @abstractmethod que, mesmo se os métodos das subclasses estejam totalmente funcionais,
        retornará ume erro pois check_answer não foi implementado. 
    """
    def __init__(self, question_id: int, text: str, theme: str, difficulty_points: int):
        raise NotImplementedError("Question class initialization is not yet implemented.")
