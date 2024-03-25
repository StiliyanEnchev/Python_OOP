class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.items = list(dictionary.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index > len(self.items) - 1:
            raise StopIteration

        return self.items[self.index]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
