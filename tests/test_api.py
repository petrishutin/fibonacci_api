import pytest

from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture(scope='session')
def client():
    with TestClient(app) as client:
        yield client


def test_fibonacci_200(client, fib_params):
    args, results = fib_params
    response = client.get(f'/fibonacci?start_from={args[0]}&to={args[1]}')
    assert response.status_code == 200, response.text
    assert response.json() == results


def test_wrong_params_400(client):
    response = client.get(f'/fibonacci?start_from=1&to=0')
    assert response.status_code == 400, response.text
