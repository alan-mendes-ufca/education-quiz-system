import requests
import pytest


def test_redirect_index_without_login():
    response = requests.get(
        "http://localhost:5000/", allow_redirects=False
    )  # Não perite redirecionamentos
    assert response.status_code in [301, 302, 401, 403]
