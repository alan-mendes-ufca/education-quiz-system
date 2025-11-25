from models.User import User 
from repositories.QuizResultRepository import QuizResultRepository
import json

class Statistics:
    """
    Responsável por gerenciar o QuizResult e construir uma estatística geral das sessões.
    - Atributos: result_repository: QuizResultRepository.
    - Métodos: get_accuracy_rate(user: User) -> float, get_player_ranking() -> list, get_most_missed_questions() -> list[Question].
    - Relacionamento/descrição: Serviço responsável por calcular informações, estatísticas das "partidas".

    """
    def __init__(self, repo: QuizResultRepository):
        self.repo = repo

    def get_accuracy_rate(self, user : User) -> int:
        """
            Calcula a taxa de acertos do usuário: total_acertos / total_pergutas_respondidas
        """
        user_history = self.repo.get_results_by_user(user) # retonar todos os quizzes que o usuário já fez!
        
        score = sum(run.get('score_achieved', 0) for run in user_history)
        total_questions = sum(len(json.loads(run.get('responses_history', 0))) for run in user_history)        
        
        # Previnindo um ZeroDivisionError
        if total_questions == 0:
            return 0.0

        return score/total_questions
