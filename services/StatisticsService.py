# models of data (encapsulation)
from models.User import User
from models.Quiz import Quiz

# Repo classes for querys.
from repositories.QuizResultRepository import QuizResultRepository
from repositories.UserAnswerRepository import UserAnswerRepository


class StatisticsService:
    """
    Responsável por gerenciar o QuizResult e construir uma estatística geral das sessões.
    - Atributos: result_repository: QuizResultRepository.
    - Métodos: get_accuracy_rate(user: User) -> float, get_player_ranking() -> list, get_most_missed_questions() -> list[Question].
    - Relacionamento/descrição: Serviço responsável por calcular informações, estatísticas das "partidas".
    - Regra de negócio: Ranking e estatísticas devem ignorar tentativas incompletas.
        - As tentativas incompletas não são salvas no banco de dados, logo não será contabilizado nas estatísticas.
         `Gera uma depedência com a camada da aplicação.`

    """

    def __init__(
        self, quiz_repo: QuizResultRepository, user_answer: UserAnswerRepository
    ):
        self.quiz_repo = quiz_repo
        self.user_answer = user_answer

    def get_accuracy_rate(self, user: User) -> float:
        """
        Calcula a taxa de acertos do usuário: total_acertos / total_pergutas_respondidas
        """
        user_history = self.quiz_repo.get_results_by_user(
            user
        )  # retonar todos os quizzes que o usuário já fez!

        # FIXING return a empty list by compatiblity with json.lodas, that gerenare type error with the `0` return
        # BEFORE: score = sum(run.get("score_achieved", 0) for run in user_history)
        score = sum(run.get("score_achieved", "[]") for run in user_history)

        total_questions = sum(
            # Ainda, é preciso fazer uma correção. A pontuação é ponderada, então devo retornar, na verdade: score_achieved / max_possible_score
            run.get("max_possible_score", "[]")
            for run in user_history
        )

        # Previnindo um ZeroDivisionError
        if total_questions == 0:
            return 0.0

        return score / total_questions

    def get_player_ranking(self):
        """
        Retorna o ranking dos 10 usuário com maior pontuação dentro todos os quizzes.
        """
        return self.quiz_repo.get_ranking()

    def get_player_ranking_by_quiz(self, quiz_result_id) -> list:
        """
        Retorna o ranking dos 10 usuário com maior pontuação em um quiz específico.
        """
        return self.quiz_repo.get_results_by_quiz(quiz_result_id)

    def get_most_missed_question_by_quiz(self, quiz_result_id):
        """
        Retorna a questão que mais erraram em um quiz específico.
        """
        return self.user_answer.get_most_missed_question_by_quiz(quiz_result_id)

    def get_most_missed_question_all(self):
        """
        Retorna a questão que mais erraram dentre todos os quizzes.
        """
        return self.user_answer.get_most_missed_question_all()

    def get_most_correct_question_by_quiz(self, quiz_result_id):
        """
        Retorna a questão que mais acertada em um quiz específico.
        """
        return self.user_answer.get_most_correct_question_by_quiz(quiz_result_id)

    def get_most_correct_question_all(self):
        """
        Retorna a questão que mais acertada dentre todos os quizzes.
        """
        return self.user_answer.get_most_correct_question_all()
