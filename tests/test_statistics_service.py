from models.User import User
from models.Quiz import Quiz
from models.QuizResult import QuizResult
from services.StatisticsService import Statistics
import pytest


@pytest.fixture
def accuracy_arrange(
    init_db, sample_user, sample_quiz_result, sample_quiz, sample_responses_history
):
    init_db
    user = sample_user
    result = sample_quiz_result
    result.save(QuizResult(user, sample_quiz, 10, 60, sample_responses_history))

    return result, user


def test_accuracy_rate(accuracy_arrange):
    result, user = accuracy_arrange

    s = Statistics(result)
    assert s.get_accuracy_rate(user) == 5


def test_accuracy_continuos_calc(
    accuracy_arrange, sample_quiz, sample_responses_history
):
    result, user = accuracy_arrange
    result.save(QuizResult(user, sample_quiz, 0, 60, sample_responses_history))

    s = Statistics(result)
    assert s.get_accuracy_rate(user) == 2.5


def test_accuracy_rate_zero_division_error(init_db, sample_user, sample_quiz_result):
    init_db
    user = sample_user
    result = sample_quiz_result
    result.save(
        QuizResult(
            user,
            Quiz(1, "Quiz de Teste", []),
            score_achieved=10,
            time_taken=30,
            responses_history=[],
        )
    )

    s = Statistics(result)
    assert s.get_accuracy_rate(user) == 0.0


def test_ranking(init_db, sample_quiz_result):
    init_db
    result = sample_quiz_result

    for i in range(1, 10):
        result.save(
            QuizResult(
                User(i, f"teste{i}", f"teste{i}@gmail.com"),
                Quiz(1, "Quiz de Teste", []),
                score_achieved=(10 - i),
                time_taken=30,
                responses_history=[],
            )
        )

    s = Statistics(result)
    assert s.get_player_ranking() is not None
    assert s.get_player_ranking_by_quiz(quiz_id=1) is not None
