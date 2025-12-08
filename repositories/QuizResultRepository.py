from models.Quiz import Quiz
from models.QuizResult import QuizResult
from models.User import User
from cs50 import SQL


import os


class QuizResultRepository:
    """
    Cadastra os resultados dos usuário no banco de dados.
    - Métodos: save(result: QuizResult), get_results_by_user(user: User) -> list[QuizResult].
    - Relacionamento/descrição: Cadastra os resultados dos usuário no banco de dados. Será consumido posteriormente ao gerar as estatísticas (StatisticsService).
    """

    def __init__(self, db_url=None):
        # Corrige o caminho para o banco de dados
        if db_url is None:
            db_path = os.path.join(
                os.path.dirname(os.path.dirname(__file__)), "data", "app.db"
            )
            db_url = f"sqlite:///{db_path}"
        self.db = SQL(db_url)

    def save(self, result: QuizResult):
        """
        Salva o resultado de um quiz no banco de dados.
        """
        return self.db.execute(
            "INSERT INTO quiz_result (user_id, quiz_id, score_achieved, time_taken, max_possible_score) VALUES (?, ?, ?, ?, ?)",
            result.user.user_id,
            result.quiz.quiz_id,
            result.score_achieved,
            result.time_taken,
            result.max_possible_score,
        )

    def get_results_by_user(self, user: User) -> list[QuizResult]:
        """
        Busca os resultados de um usuário.
        """
        try:
            results = self.db.execute(
                "SELECT * FROM quiz_result WHERE user_id = ?", user.user_id
            )
        except Exception as e:
            raise e("Erro ao buscar resultados do quiz")
        return results

    def get_results_by_quiz(self, quiz_id) -> list[QuizResult]:
        """
        Retorna o score de todos os usuários que responderam um quiz específico.
        """
        return self.db.execute(
            "SELECT user_id, SUM(score_achieved) as total_score "
            "FROM quiz_result "
            "WHERE quiz_id = ? "
            "GROUP BY user_id "
            "ORDER BY total_score DESC "
            "LIMIT 10; ",
            quiz_id,
        )

    def get_ranking(self) -> list:
        """
        Retorna um ranking geral somando todas as pontuações já obtidas.
        """
        return self.db.execute(
            (
                "SELECT user_id, SUM(score_achieved) as total_score "
                "FROM quiz_result "
                "GROUP BY user_id "
                "ORDER BY total_score DESC "
                "LIMIT 10;"
            )
        )
