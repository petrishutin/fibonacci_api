import pytest

from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture(scope='session')
def client():
    with TestClient(app) as client:
        yield client


@pytest.mark.parametrize(
    "args, results",
    (
            ([0, 0], [0]),
            ([0, 1], [0, 1]),
            ([0, 2], [0, 1, 1]),
            ([1, 3], [1, 1, 2])
    )
)
def test_fibonacci_200(client, args, results):
    response = client.get(f'/fibonacci?start_from={args[0]}&to={args[1]}', )
    assert response.status_code == 200, response.text
    assert response.json() == results
