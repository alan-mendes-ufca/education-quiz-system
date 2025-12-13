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
        current_questiton_index: int = 0,
    ):
        self.quiz = quiz
        self.user = user
        self.current_question_index = current_questiton_index
        self.score = 0

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

        result = self.get_current_question().check_answer(user_response.selected_option)

        self.score += result["score"]

        user_response.is_correct = result["is_correct"]

        self.register_user_response_repo.save(user_response)

        self.register_time(user_response.time_to_response)

        if self.current_question_index < len(self.quiz.questions) - 1:
            self.current_question_index += 1
        else:
            return self.finish_game()

        return self.get_current_question()

    def register_time(self, time_to_response: float):
        self.time.append({self.current_question_index: time_to_response})

    def finish_game(self):
        self.register_quiz_result.save(
            QuizResult(
                self.user, self.quiz, self.score, self.time, self.quiz.get_max_score()
            )
        )
        return None
