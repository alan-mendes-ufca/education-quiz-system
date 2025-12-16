import requests
import cs50
import pytest


URL = "http://127.0.0.1:5000/quiz/save"


def test_save_quiz_get():
    # GET: método inválido para essa rota.
    response = requests.get(URL)
    assert response.status_code == 405


def test_save_quiz_post():
    # POST
    data = {
        "title": "Quiz de Teste",
        "category": "Geral",
        "description": "Um quiz criado para testes automatizados.",
        "questions": [
            {
                "proposition": "Qual é a capital da França?",
                "category": "Geral",
                "alternatives": ["Berlim", "Madrid", "Paris", "Lisboa"],
                "correct_option_index": 2,
                "difficulty_points": 3,
            },
            {
                "proposition": "Qual é 2 + 2?",
                "category": "Geral",
                "alternatives": ["3", "4", "5", "6"],
                "correct_option_index": 1,
                "difficulty_points": 2,
            },
        ],
    }

    # Validar no banco de dados.

    pytest.skip("Banco de dados não configurado para testes automatizados.")
    response = requests.post(URL, json=data)
    assert response.status_code == 200
