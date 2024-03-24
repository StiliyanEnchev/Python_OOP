class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.end_index = len(self.iterable)
        self.start_index = 0

    def __iter__(self):
        return reversed(self.iterable)

    def __next__(self):
        if self.end_index > self.start_index:
            self.end_index -= 1
            return self.iterable[self.end_index]
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
