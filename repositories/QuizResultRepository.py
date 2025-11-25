from models.Quiz import Quiz
from models.QuizResult import QuizResult
from models.User import User
from cs50 import SQL

class QuizResultRepository:
    """
        Cadastra os resultados dos usuário no banco de dados. 
        - Métodos: save(result: QuizResult), get_results_by_user(user: User) -> list[QuizResult].
        - Relacionamento/descrição: Cadastra os resultados dos usuário no banco de dados. Será consumido posteriormente ao gerar as estatísticas (StatisticsService).
    """

    def __init__(self, db_url="sqlite:///app.db"):
        self.db = SQL(db_url)
    
    def save(self, result: QuizResult):        
        return self.db.execute("INSERT INTO quiz_result (user_id, quiz_id, score_achieved, time_taken, responses_history) VALUES (?, ?, ?, ?, ?)", result.user.user_id, result.quiz.quiz_id, result.score_achieved, result.time_taken, result.responses_history)
    
    def get_results_by_user(self, user: User) -> list[QuizResult]:
        try:
            results = self.db.execute("SELECT * FROM quiz_result WHERE user_id = ?", user.user_id)
        except Exception as e:
            raise e("Erro ao buscar resultados do quiz")
        return results 
    
    def get_results_by_quiz(self, quiz: Quiz) -> list[QuizResult]:
        try:
            results = self.db.execute("SELECT * FROM quiz_result WHERE quiz_id = ?", quiz.quiz_id)
        except Exception as e:
            raise e("Erro ao buscar resultados do quiz")
        return results
    