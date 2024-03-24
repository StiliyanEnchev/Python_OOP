def squares(number):
    for num in range(number):
        num += 1
        yield num * num

print(list(squares(5)))