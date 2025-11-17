from .Question import Question

class Quiz:
    """
        Responsável por guardar os dados do quiz.
        - Por que recebe list[Question] sendo que as perguntas do quiz serão apenas de múltipla escolha(MultipleChoice)?
        Basicamente, MultipleChoice é uma classe filha de Question, ou seja ela também é uma question. Também abre flexibilidade para
        a utilização de outros tipos de pergunta como verdadeira ou falsa e por extenso.
    """
    def __init__(self, quiz_id: int, title: str, questions: list[Question]):
        raise NotImplementedError("Unimplemented feature.")