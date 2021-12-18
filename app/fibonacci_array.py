from typing import Tuple, Dict

from app.finbonacci_generator import FibonacciGenerator


def build_fibonacci_array(fib_storage: Dict[int, Tuple[int, int]], start_from: int = 0, end_at: int = 0):
    def _get_last_key_in_storage():
        try:
            return max(fib_storage.keys())
        except ValueError:
            fib_storage[0] = (0, 1)
            return 0

    def _fill_storage_to_number(last_key: int):
        first_key = _get_last_key_in_storage()
        first_item = fib_storage[first_key]
        fib_gen = FibonacciGenerator(*first_item)
        for key in range(first_key + 1, last_key + 1):
            fib_storage[key] = next(fib_gen)

    if end_at > _get_last_key_in_storage():
        _fill_storage_to_number(last_key=end_at)

    if start_from == 0 and end_at == 0:
        return [0]
    results = []
    arr_range = [i for i in range(start_from, end_at + 1)]
    for number in arr_range:
        results.append(fib_storage[number][0])
    return results
