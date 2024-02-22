n = int(input())


def print_upped_part(size):
    for row in range(1, size + 1):
        print(' ' * (size-row), '* ' * row)


def print_lower_part(size):
    for row in range(size - 1, 0, -1):
        print(' ' * (size - row), '* ' * row)


def print_rhombus(size):
    print_upped_part(size)
    print_lower_part(size)


print_rhombus(n)