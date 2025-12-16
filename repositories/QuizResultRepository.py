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
            "INSERT INTO quiz_result (user_id, quiz_id, session_id, score_achieved, time_taken, max_possible_score) VALUES (?, ?, ?, ?, ?, ?)",
            result.user.user_id,
            result.quiz.quiz_id,
            result.quiz_session,
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
            raise Exception(f"Erro ao buscar: {e}")
        return results

    def get_results_by_quiz(self, quiz_id) -> list[QuizResult]:
        """
        Retorna o score de todos os usuários que responderam um quiz específico.
        """
        return self.db.execute(
            "SELECT "
            "  u.id AS user_id, "
            "  u.name AS user_name, "
            "  u.email AS user_email, "
            "  SUM(qr.score_achieved) AS total_score, "
            "  SUM(qr.max_possible_score) AS total_max_possible_score, "
            "  SUM(qr.time_taken) AS total_time_taken "
            "FROM quiz_result qr "
            "JOIN user u ON u.id = qr.user_id "
            "WHERE qr.quiz_id = ? "
            "GROUP BY u.id, u.name, u.email "
            "ORDER BY total_score DESC "
            "LIMIT 10; ",
            quiz_id,
        )

    def get_results_by_session(self, session_id) -> dict:
        """
        Retorna os dados completos de uma sessão para exibir na tela de resultado.
        Inclui: quiz (id, title), user (id, name), score, max_score, time_taken.
        """
        rows = self.db.execute(
            "SELECT "
            "  qr.session_id, "
            "  qr.score_achieved AS score, "
            "  qr.max_possible_score AS max_score, "
            "  qr.time_taken, "
            "  q.id AS quiz_id, "
            "  q.title AS quiz_title, "
            "  q.category AS quiz_category, "
            "  u.id AS user_id, "
            "  u.name AS user_name "
            "FROM quiz_result qr "
            "JOIN quiz q ON q.id = qr.quiz_id "
            "JOIN user u ON u.id = qr.user_id "
            "WHERE qr.session_id = ?;",
            session_id,
        )
        if not rows:
            return None
        row = rows[0]
        return {
            "quiz": {
                "id": row["quiz_id"],
                "title": row["quiz_title"],
                "category": row["quiz_category"],
            },
            "user": {
                "id": row["user_id"],
                "name": row["user_name"],
            },
            "score": row["score"],
            "max_score": row["max_score"],
            "time_taken": row["time_taken"],
            "passed": row["score"] >= (row["max_score"] * 0.5),  # 50% para passar
        }

    def get_ranking(self) -> list:
        """
        Retorna um ranking geral somando todas as pontuações já obtidas.
        """

        result = self.db.execute(
            "SELECT "
            "  u.id AS user_id, "
            "  u.name AS user_name, "
            "  u.email AS user_email, "
            "  SUM(qr.score_achieved) AS total_score, "
            "  SUM(qr.max_possible_score) AS total_max_possible_score, "
            "  SUM(qr.time_taken) AS total_time_taken "
            "FROM quiz_result qr "
            "JOIN user u ON u.id = qr.user_id "
            "GROUP BY u.id, u.name, u.email "
            "ORDER BY total_score DESC "
            "LIMIT 10;"
        )

        return result
