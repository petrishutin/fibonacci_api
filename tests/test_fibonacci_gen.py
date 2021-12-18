from app.finbonacci_generator import FibonacciGenerator


def test_fibonacci_gen():
    fib_gen = FibonacciGenerator()
    assert next(fib_gen) == (1, 1)
    assert next(fib_gen) == (1, 2)
    assert next(fib_gen) == (2, 3)


def test_start_fib_gen_with_params():
    fib_gen = FibonacciGenerator(1, 2)
    assert next(fib_gen) == (2, 3)
