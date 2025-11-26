import pytest

from cs50 import SQL
from models.Quiz import Quiz
from models.User import User
from repositories.QuizResultRepository import QuizResultRepository

DB_PATH = r"db/test_statistics_db.sqlite"
DB_URL = f"sqlite:///{DB_PATH}"


def _schema(db: SQL):
    db.execute("DROP TABLE IF EXISTS quiz_result;")
    db.execute("DROP TABLE IF EXISTS user_answer;")

    db.execute(
        """
        CREATE TABLE quiz_result ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            user_id INTEGER NOT NULL, 
            quiz_id INTEGER NOT NULL, 
            score_achieved INTEGER NOT NULL, 
            time_taken REAL NOT NULL, 
            responses_history json NOT NULL
        );
        """
    )

    db.execute(
        """
        CREATE TABLE user_answer( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            quiz_id INTEGER NOT NULL,
            question_id INTEGER NOT NULL,
            selected_option INTEGER NOT NULL,
            is_correct BOOLEAN NOT NULL,
            FOREIGN KEY (quiz_id) REFERENCES quiz(id),
            FOREIGN KEY (question_id) REFERENCES multiple_choice_question(id)
        );
        """
    )


@pytest.fixture
def init_db():
    database = SQL(DB_URL)
    _schema(database)
    return database


@pytest.fixture
def sample_user():
    return User(1, "teste", "teste@gmail.com")


@pytest.fixture
def sample_quiz():
    return Quiz(1, "Quiz de Teste", [])


@pytest.fixture
def sample_quiz_result():
    return QuizResultRepository(DB_URL)


@pytest.fixture
def sample_responses_history():
    # Aqui eu defini um padrão para o histórico de perguntas do usuário.
    # deve ter correspondência nas outras camadas.
    return [
        {
            "question_id": 1,
            "selected_option": 2,
            "is_correct": True,
            "time_spent": 15.2,
        },
        {
            "question_id": 2,
            "selected_option": 0,
            "is_correct": True,
            "time_spent": 10.5,
        },
    ]
