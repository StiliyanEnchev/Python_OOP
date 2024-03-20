class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current_num = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_num += 1
        if self.current_num <= self.end:
            return self.current_num
        raise StopIteration


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
