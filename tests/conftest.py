import pytest


@pytest.fixture(
    params=[
        ([0, 0], [0]),
        ([0, 1], [0, 1]),
        ([0, 2], [0, 1, 1]),
        ([1, 3], [1, 1, 2])
    ]
)
def fib_params(request):
    return request.param
