from http import HTTPStatus
from fastapi.testclient import (
    TestClient,
)  # primeiro as inimprotacoex esxternas

from fastapi_zero.app import app


def test_root():
    """Triple A: arrange A: act A: assert"""
    #arrange: organiza o setup
    client = TestClient(app)
    #act: o que esta sendo testado

    response = client.get('/')
    #assert: afirma, garante que algo é algo

    assert response.json() == {'message': 'Hello, World'}
    assert response.status_code == HTTPStatus.OK
