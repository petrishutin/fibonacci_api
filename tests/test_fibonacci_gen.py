from app.finbonacci_generator import FibonacciGenerator


def test_fibonacci_gen():
    fib_gen = FibonacciGenerator()
    assert next(fib_gen) == {'count': 1, 'prev': 1, 'curr': 1}
    assert next(fib_gen) == {'count': 2, 'prev': 1, 'curr': 2}
    assert next(fib_gen) == {'count': 3, 'prev': 2, 'curr': 3}


def test_start_fib_gen_with_params():
    fib_gen = FibonacciGenerator(2, 1, 2)
    assert next(fib_gen) == {'count': 3, 'prev': 2, 'curr': 3}
