import requests


def test_quizzes_api_get():
    response = requests.get("http://localhost:5000/api/quizzes")
    assert response.status_code == 200
    quizzes = response.json()
    assert isinstance(quizzes, list)


def test_quizzes_api_invalid_method():
    response = requests.post("http://localhost:5000/api/quizzes")
    assert response.status_code == 405


def test_quizzes_search_by_category():
    category = "javascript"
    response = requests.get(
        f"http://localhost:5000/api/quizzes/search?category={category}"
    )
    assert response.status_code == 200
    quizzes = response.json()
    assert isinstance(quizzes, list)
    for quiz in quizzes:
        assert quiz.get("category") == category


def test_quizzes_search_no_category():
    response = requests.get("http://localhost:5000/api/quizzes/search")
    assert response.status_code == 200
    quizzes = response.json()
    assert quizzes == []
