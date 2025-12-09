
from models.Question import Question
from models.Quiz import Quiz
from repositories.QuestionRepository import QuestionRepository
from repositories.QuizRepository import QuizRepository


class QuizService:
    def __init__(self):
        self.quiz_repo = QuizRepository
        self.question_repo = QuestionRepository

    def save_questions(self, quiz: Quiz):
        for question in quiz.questions:
            self.question_repo.create(question)

    def save_quiz(self, quiz: Quiz):
        self.save_questions(quiz)
        self.quiz_repo.create(quiz)