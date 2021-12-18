class FibonacciGenerator:

    def __init__(self, count: int = 0, prev: int = 0, curr: int = 1):
        self.count = count
        self.prev = prev
        self.curr = curr

    def __next__(self):
        self.count += 1
        self.prev, self.curr = self.curr, self.prev + self.curr
        return {'count': self.count, 'prev': self.prev, 'curr': self.curr}

    next = __next__
    set_state = __init__
