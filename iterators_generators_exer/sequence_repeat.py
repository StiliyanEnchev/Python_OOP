class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number + 1
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):

        while self.number >= 0:
            self.index += 1
            self.number -= 1

            if self.number == 0:
                raise StopIteration

            try:
                return self.sequence[self.index]
            except IndexError:
                self.index = 0
                return self.sequence[self.index]




result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
