def genrange(start, end):
    while end >= start:
        yield start
        start += 1


print(list(genrange(1, 10)))