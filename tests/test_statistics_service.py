from cs50 import SQL
from models.Quiz import Quiz
from models.User import User
from models.QuizResult import QuizResult
from services.StatisticsService import Statistics
from repositories.QuizResultRepository import QuizResultRepository

# REFATORAR DEPOIS

db_url = "sqlite:///" + "db/test_statistics_db.sqlite"


def reset_db():
    db = SQL(db_url)
    db.execute("DROP TABLE IF EXISTS quiz_result;")
    db.execute(
        "CREATE TABLE quiz_result ( "
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "user_id INTEGER NOT NULL, "
        "quiz_id INTEGER NOT NULL, "
        "score_achieved INTEGER NOT NULL, "
        "time_taken REAL NOT NULL, "
        "responses_history json NOT NULL);"
    )


def test_accuracy_rate():
    reset_db()

    u = User(1, "teste", "teste@gmail.com")

    result = QuizResultRepository(db_url)
    result.save(
        QuizResult(
            u,
            Quiz(1, "Quiz de Teste", []),
            score_achieved=10,
            time_taken=30,
            # passing json string becouse .execute just suport simple data (int, str, ...).
            responses_history='[{"0": "Pergunta0: Hello Words!"}]',
        )
    )

    s = Statistics(result)
    assert s.get_accuracy_rate(u) == 10

    # Validando cálculo contínuo de accuracy_rate.
    result.save(
        QuizResult(
            u,
            Quiz(1, "Quiz de Teste", []),
            score_achieved=0,
            time_taken=30,
            responses_history='[{"0": "Pergunta0: Hello Words!"}]',
        )
    )
    assert s.get_accuracy_rate(u) == 5


def test_accuracy_rate_zero_divison_error():
    reset_db()
    u = User(1, "teste", "teste@gmail.com")

    result = QuizResultRepository(db_url)
    result.save(
        QuizResult(
            u,
            Quiz(1, "Quiz de Teste", []),
            score_achieved=10,
            time_taken=30,
            # passing a empty list to test a zeroDivisionError
            responses_history="[]",
        )
    )

    s = Statistics(result)
    assert s.get_accuracy_rate(u) == 0.0


def test_raking():
    result = QuizResultRepository(db_url)

    for i in range(1, 10):
        result.save(
            QuizResult(
                User(i, "teste", "teste@gmail.com"),
                Quiz(1, "Quiz de Teste", []),
                score_achieved=(10 - i),
                time_taken=30,
                # passing a empty list to test a zeroDivisionError
                responses_history="[]",
            )
        )

    s = Statistics(result)
    assert s.get_player_ranking is not None
    assert s.get_player_ranking_by_quiz(quiz_id=1) is not None
