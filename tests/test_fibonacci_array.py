import pytest

from app.fibonacci_array import build_fibonacci_array


@pytest.mark.parametrize(
    'last_number, results',
    (
            (0, {0: (0, 1)}),
            (3, {0: (0, 1), 1: (1, 1), 2: (1, 2), 3: (2, 3)})
    )
)
def test_fill_empty_storage(last_number, results):
    fibonacci_storage = dict()
    build_fibonacci_array(fibonacci_storage, 0, last_number)
    assert fibonacci_storage == results


def test_fill_not_empty_storage():
    fibonacci_storage = {0: (0, 1), 1: (1, 1), 2: (1, 2)}
    build_fibonacci_array(fibonacci_storage, 0, 3)
    assert fibonacci_storage == {0: (0, 1), 1: (1, 1), 2: (1, 2), 3: (2, 3)}


def test_fibonacci_array(fib_params):
    args, results = fib_params
    fibonacci_storage = dict()
    assert build_fibonacci_array(fibonacci_storage, *args) == results
