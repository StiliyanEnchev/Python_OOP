class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.number = 0 - self.step
        self.iters = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += self.step
        self.iters += 1

        if self.iters < self.count:
            return self.number
        raise StopIteration

numbers = take_skip(2, 6)
for number in numbers:
    print(number)
