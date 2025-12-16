from models.User import User
from models.UserAnswer import UserAnswer
from models.Quiz import Quiz
from models.QuizResult import QuizResult
from services.StatisticsService import StatisticsService
import pytest
from cs50 import SQL

from repositories.UserAnswerRepository import UserAnswerRepository
from repositories.QuizResultRepository import QuizResultRepository

DB_PATH = r"db/test_statistics_db.sqlite"
DB_URL = f"sqlite:///{DB_PATH}"


def _schema(db: SQL):
    db.execute("DROP TABLE IF EXISTS quiz_result;")
    db.execute("DROP TABLE IF EXISTS user_answer;")
    db.execute("DROP TABLE IF EXISTS user;")

    db.execute(
        """
        CREATE TABLE user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL UNIQUE
        );
        """
    )

    db.execute(
        """
        CREATE TABLE quiz_result ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            user_id INTEGER NOT NULL, 
            quiz_id INTEGER NOT NULL, 
            session_id INTEGER NOT NULL,
            score_achieved INTEGER NOT NULL, 
            time_taken REAL NOT NULL, 
            max_possible_score INT NOT NULL
        );
        """
    )

    db.execute(
        """
        CREATE TABLE user_answer ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            user_id INTEGER NOT NULL,
            quiz_id INTEGER NOT NULL,
            question_id INTEGER NOT NULL,
            selected_option INTEGER NOT NULL,
            is_correct BOOLEAN NOT NULL,
            time_to_response FLOAT
            -- FOREIGN KEY (user_id) REFERENCES user(id), 
            -- FOREIGN KEY (quiz_id) REFERENCES quiz(id),
            -- FOREIGN KEY (question_id) REFERENCES multiple_choice_question(id)
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
def sample_quiz_session(sample_user, sample_quiz):
    return 1


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


@pytest.fixture
def max_possible_score():
    pass


@pytest.fixture
def accuracy_arrange(
    init_db, sample_user, sample_quiz_result, sample_quiz, sample_quiz_session
):
    """
    ARRENGE: where we prepair the entire context for our tests.
    """

    init_db
    user = sample_user
    result = sample_quiz_result
    result.save(QuizResult(user, sample_quiz, sample_quiz_session, 10, 60, 10))

    return result, user


def test_accuracy_rate(accuracy_arrange):
    result, user = accuracy_arrange

    """
    ACTION: init the function that we have to test.  
    """
    s = StatisticsService(result, UserAnswerRepository(DB_URL))

    """
    Assert: verify if the results are like the presupose.
    """
    assert s.get_accuracy_rate(user) == 1


def test_accuracy_continuos_calc(accuracy_arrange, sample_quiz):
    # Like a different quizzes, because every line is an diferent quiz result.
    # In other words, the accuracy rate is about the whole story.
    result, user = accuracy_arrange
    result.save(
        QuizResult(
            user,
            sample_quiz,
            2,
            0,
            60,
            10,
        )
    )

    s = StatisticsService(result, UserAnswerRepository(DB_URL))
    assert s.get_accuracy_rate(user) == 0.5


def test_accuracy_rate_zero_division_error(init_db, sample_user, sample_quiz_result):
    init_db
    user = sample_user
    result = sample_quiz_result
    result.save(
        QuizResult(
            user,
            Quiz(1, "Quiz de Teste", []),
            1,
            10,
            30,
            0,
        )
    )

    s = StatisticsService(result, UserAnswerRepository(DB_URL))
    assert s.get_accuracy_rate(user) == 0.0


def test_ranking(init_db, sample_quiz_result):
    init_db
    result = sample_quiz_result

    for i in range(1, 10):
        result.save(
            QuizResult(
                User(i, f"teste{i}", f"teste{i}@gmail.com"),
                Quiz(1, "Quiz de Teste", []),
                i,
                (10 - i),
                0,
                10,
            )
        )

    s = StatisticsService(result, UserAnswerRepository(DB_URL))
    assert s.get_player_ranking() is not None
    assert s.get_player_ranking_by_quiz(1) is not None


@pytest.fixture
def sample_user_answer_repo():
    return UserAnswerRepository(DB_URL)


# tests of get the most missed, or correct, question, by quiz or in the whole history of runs.
def test_most_missed_question_by_quiz(init_db, sample_user_answer_repo):

    db = init_db

    # I dont will init the foreign repos, I only commendted the lines that supose the foreign keys.
    # insert questions on user_answer table(user_id, quiz_result_id, question_id, selected_option, is_correct).
    user_answer_repo = sample_user_answer_repo

    for i in range(1, 11):
        user_answer_repo.save(UserAnswer(i, 2, 2, 3, False))
        if i < 8:
            user_answer_repo.save(UserAnswer(i, 2, 3, 3, False))

    st = StatisticsService(sample_quiz_result, user_answer_repo)

    assert (
        st.get_most_missed_question_by_quiz(quiz_result_id=2)[0].get("question_id") == 2
    )
    assert (
        st.get_most_missed_question_by_quiz(quiz_result_id=2)[0].get("miss_count") == 10
    )


def test_most_missed_question_all(init_db, sample_user_answer_repo):
    db = init_db
    user_answer_repo = sample_user_answer_repo

    for i in range(1, 11):
        user_answer_repo.save(UserAnswer(i, 2, 2, 3, False))
        if i == 10:
            for j in range(1, 21):
                user_answer_repo.save(
                    UserAnswer(j, 3, 3, 3, False)
                )  # Questão mais errada

    st = StatisticsService(sample_quiz_result, user_answer_repo)

    assert st.get_most_missed_question_all()[0].get("question_id") == 3
    assert st.get_most_missed_question_all()[0].get("miss_count") == 20


def test_most_correct_question_by_quiz(init_db, sample_user_answer_repo):
    db = init_db
    user_answer_repo = sample_user_answer_repo

    for i in range(1, 11):
        user_answer_repo.save(UserAnswer(i, 3, 2, 3, True))
        if i == 10:
            for j in range(1, 21):
                user_answer_repo.save(
                    UserAnswer(j, 3, 3, 3, False)
                )  # Questão mais errada

    st = StatisticsService(sample_quiz_result, user_answer_repo)

    assert st.get_most_correct_question_by_quiz(3)[0].get("question_id") == 2
    assert st.get_most_correct_question_by_quiz(3)[0].get("count_correct") == 10


def test_most_correct_question_all(init_db, sample_user_answer_repo):
    db = init_db
    user_answer_repo = sample_user_answer_repo

    for i in range(1, 11):
        user_answer_repo.save(UserAnswer(i, 3, 2, 3, True))
        if i == 10:
            for j in range(1, 21):
                user_answer_repo.save(
                    UserAnswer(j, 3, 3, 3, True)
                )  # Questão mais errada

    st = StatisticsService(sample_quiz_result, user_answer_repo)

    assert st.get_most_correct_question_all()[0].get("question_id") == 3
    assert st.get_most_correct_question_all()[0].get("count_correct") == 20
