from models.Question import Question
from models.MultipleChoice import MultipleChoiceQuestion
from models.Quiz import Quiz
from models.QuizResult import QuizResult
from models.User import User
from models.UserAnswer import UserAnswer

from repositories.UserAnswerRepository import UserAnswerRepository
from repositories.QuizResultRepository import QuizResultRepository


class QuizGame:
    """
    - Atributos: quiz: Quiz, user: User, current_question_index: int.
    - Métodos: start_game(), get_current_question() -> Question, submit_answer(answer), finish_game() -> QuizResult (cria e retorna um objeto QuizResult).

    - Relacionamento/descrição: Controla o estado e o fluxo de uma única sessão de jogo. É responsável por avançar as perguntas, registrar as respostas
    do usuário e, ao final (finish_game), criar e retornar o objeto QuizResult.

    - Regras de negócio:
        - O usuário não pode realizar um quiz mais vezes que o limite configurado.
        - Se o tempo limite for excedido, o quiz é encerrado automaticamente.
        - Ranking e estatísticas devem ignorar tentativas incompletas.


    """

    def __init__(
        self,
        quiz: Quiz = None,
        user: User = None,
        current_question_index: int = 0,
        session_id: int = None,
    ):
        self.quiz = quiz
        self.user = user
        self.current_question_index = current_question_index
        self.score = 0
        self.session_id = session_id

        self.register_user_response_repo = UserAnswerRepository()
        self.register_quiz_result = QuizResultRepository()

        self.time = []

    def start_game(self):
        """
        Inicia a rodada.
        """
        return self.get_current_question()

    def get_current_question(self) -> MultipleChoiceQuestion:
        return self.quiz.questions[self.current_question_index]

    def register_user_response(self, user_response: UserAnswer):

        print("SELECTED OPTION:", user_response.selected_option)
        result = self.get_current_question().check_answer(user_response.selected_option)

        self.score += result["score"]

        user_response.is_correct = result["is_correct"]

        self.register_user_response_repo.save(user_response)

        self.register_time(user_response.time_to_response)

        if self.current_question_index < len(self.quiz.questions) - 1:
            self.current_question_index += 1
        else:
            return None

        return self.get_current_question()

    def register_time(self, time_to_response: float):
        self.time.append({self.current_question_index: time_to_response})

    def get_total_time(self) -> float:
        """Calcula o tempo total somando todos os tempos de resposta."""
        return sum(list(t.values())[0] for t in self.time)

    def finish_game(self, d: dict = None):
        self.register_quiz_result.save(
            QuizResult(
                user=d.get("user") if d else self.user,
                quiz=d.get("quiz") if d else self.quiz,
                quiz_session=d.get("quiz_session") if d else self.session_id,
                score_achieved=d.get("score_achieved") if d else self.score,
                time_taken=d.get("time_taken") if d else self.get_total_time(),
                max_possible_score=(
                    d.get("max_possible_score") if d else self.quiz.get_max_score()
                ),
            ),
        )
        return None
