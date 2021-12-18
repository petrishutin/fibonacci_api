class FibonacciGenerator:

    def __init__(self, curr_v: int = 0, next_v: int = 1):
        self.curr_v = curr_v
        self.next_v = next_v

    def __next__(self):
        self.curr_v, self.next_v = self.next_v, self.curr_v + self.next_v
        return self.curr_v, self.next_v
