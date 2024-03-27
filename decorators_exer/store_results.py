class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        with open('files/log.txt', 'a') as log_file:
            log_file.write(f'Function {self.func.__name__} was called. Result: {self.func(*args, **kwargs)}')


@store_results
def sum_numbers(a, b):
    return a + b

sum_numbers(4, 6)