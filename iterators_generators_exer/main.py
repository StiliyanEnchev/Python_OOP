class MyList:

    def __init__(self, my_list):
        self.my_list = my_list
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.my_list) - 1:
            raise StopIteration

        self.index += 1

        return self.my_list[self.index]


my_list = MyList([1, 2, 3])

for el in my_list:
    print(el)