from .Question import Question

class Quiz:
    """
        Responsável por guardar os dados do quiz.
        - Por que recebe list[Question] sendo que as perguntas do quiz serão apenas de múltipla escolha(MultipleChoice)?
        Basicamente, MultipleChoice é uma classe filha de Question, ou seja ela também é uma question. Também abre flexibilidade para
        a utilização de outros tipos de pergunta como verdadeira ou falsa e por extenso.
    """
    def __init__(self, quiz_id: int, title: str, questions: list[Question]):
        self.quiz_id = quiz_id
        self.title = title
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
        score = 0
        for question in self.questions:
            score += question.difficulty_points

        return score
        
