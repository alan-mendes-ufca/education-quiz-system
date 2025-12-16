import json
from models.MultipleChoice import MultipleChoiceQuestion
from models.Question import Question
from cs50 import SQL
import os


class QuestionRepository:
    """
    Responsável pelo percistẽncia(CRUD) das questões cadastradas.
    - Métodos: create(question: Question), get_by_category(category) -> list[Question], get_random_questions(category, count) -> list[Question].
    - Relacionamento/descrição: Além do CRUD básico (persistência), ele fornece métodos de consulta especializados (ex: get_random_questions) que serão consumidos pelos serviços."

    > Herança e polimorfismo
    QuestionRepository, na verdade, refere-se a MultipleChoiceQuestionRepository.
    - Como MultipleChoiceQuestion herda de Question, ele será aceito pelo QuestionRepository.

    - Exemplo creat(self, question: Question) -> Question:...
        - Nesse caso, o método espera receter e devolverá uma instância Question.
         Mas como MultipleChoice é uma subclasse de Question, o método aceitará normalmente.

    - regras de negócio: Cada pergunta deve ter entre 3 e 5 alternativas,
     o índice da resposta correta deve corresponder a um índice existente.
    """

    def __init__(self, db_url=None):
        # Corrige o caminho para o banco de dados
        if db_url is None:
            db_path = os.path.join(
                os.path.dirname(os.path.dirname(__file__)), "data", "app.db"
            )
            db_url = f"sqlite:///{db_path}"
        self.db = SQL(db_url)

    def create(self, question: MultipleChoiceQuestion) -> Question:
        """
        Se disponível, adiciona uma questão ao repositório.
        """

        # Cada pergunta deve ter de 3 a 5 alternativas.
        if not (3 <= len(question.alternatives) <= 5):
            raise ValueError("Alternativas insuficientes!")

        # O índice da resposta correta deve corresponder a um índice existente.
        if not question.alternatives[question.correct_option_index]:
            raise ValueError("O índice para alternativa correta não está definido.")

        try:
            self.db.execute(
                "INSERT INTO multiple_choice_question (id, proposition, category, difficulty_points, alternatives, correct_option_index) VALUES (?, ?, ?, ?, ?, ?)",
                question.question_id,
                question.proposition,
                question.category,
                question.difficulty_points,
                json.dumps(question.alternatives),
                question.correct_option_index,
            )
        except ValueError:
            raise ValueError("Question already exists.")

        return self.get_by_proposition(question.proposition)

    def get_by_proposition(self, proposition) -> Question:
        """
        Seleciona um questão por enunciado específicado.
        """
        # ------ LEMBRETE : User like
        rows = self.db.execute(
            "SELECT * FROM multiple_choice_question WHERE proposition = ?", proposition
        )
        if not rows:
            return None
        return MultipleChoiceQuestion.from_dict(rows[0])

    def get_by_category(self, category) -> list[Question]:
        """
        Seleciona um questão por tema específicado.
        """
        rows = self.db.execute(
            "SELECT * FROM multiple_choice_question WHERE category = ?", category
        )
        if not rows:
            return None
        return [MultipleChoiceQuestion.from_dict(row) for row in rows]

    def get_random_questions(self, category, count) -> list[Question]:
        """
        Retorna questões aleatórias sobre um deeterminado tema.
        """
        rows = self.db.execute(
            "SELECT * FROM multiple_choice_question WHERE category = ? ORDER BY RANDOM() LIMIT ?",
            category,
            count,
        )
        if not rows:
            return None
        return [MultipleChoiceQuestion.from_dict(row) for row in rows]
