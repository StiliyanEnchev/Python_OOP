def type_check(received_type):
    def decorator(function):
        def wrapper(num):
            if isinstance(num, received_type):
                return function(num)
            return 'Bad Type'
        return wrapper

    return decorator




@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
