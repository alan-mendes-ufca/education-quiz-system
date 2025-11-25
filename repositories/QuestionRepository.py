from models.MultipleChoice import MultipleChoiceQuestion
from models.Question import Question
from cs50 import SQL


class QuestionRepository:
    """
    Responsável pelo percistẽncia(CRUD) das questões cadastradas.
    - Métodos: create(question: Question), get_by_theme(theme) -> list[Question], get_random_questions(theme, count) -> list[Question].
    - Relacionamento/descrição: Além do CRUD básico (persistência), ele fornece métodos de consulta especializados (ex: get_random_questions) que serão consumidos pelos serviços."

    > Herança e polimorfismo
    QuestionRepository, na verdade, refere-se a MultipleChoiceQuestionRepository.
    - Como MultipleChoiceQuestion herda de Question, ele será aceito pelo QuestionRepository.

    - Exemplo creat(self, question: Question) -> Question:...
        - Nesse caso, o método espera receter e devolverá uma instância Question.
         Mas como MultipleChoice é uma subclasse de Question, o método aceitará normalmente.
    """

    def __init__(self, db_url="sqlite:///app.db"):
        self.db = SQL(db_url)

    def create(self, question: Question) -> Question:
        """
        Se disponível, adiciona uma questão ao repositório.
        """
        try:
            self.db.execute(
                "INSERT INTO multiple_choice_question (proposition, theme, difficulty_points, options, correct_option_index) VALUES (?, ?, ?, ?, ?)",
                question.proposition,
                question.theme,
                question.difficulty_points,
                question.options,
                question.correct_option_index,
            )
        except ValueError:
            raise ValueError("Question already exists.")

        return self.get_by_proposition(question.proposition)

    def get_by_proposition(self, proposition) -> Question:
        """
        Seleciona um questão por enunciado específicado.
        """
        rows = self.db.execute(
            "SELECT * FROM multiple_choice_question WHERE proposition = ?", proposition
        )
        if not rows:
            return None
        return MultipleChoiceQuestion.constructor_dict(rows[0])

    def get_by_theme(self, theme) -> list[Question]:
        """
        Seleciona um questão por tema específicado.
        """
        rows = self.db.execute(
            "SELECT * FROM multiple_choice_question WHERE theme = ?", theme
        )
        if not rows:
            return None
        return [MultipleChoiceQuestion.constructor_dict(row) for row in rows]

    def get_random_questions(self, theme, count) -> list[Question]:
        """
        Retorna questões aleatórias sobre um deeterminado tema.
        """
        rows = self.db.execute(
            "SELECT * FROM multiple_choice_question WHERE theme = ? ORDER BY RANDOM() LIMIT ?",
            theme,
            count,
        )
        if not rows:
            return None
        return [MultipleChoiceQuestion.constructor_dict(row) for row in rows]
