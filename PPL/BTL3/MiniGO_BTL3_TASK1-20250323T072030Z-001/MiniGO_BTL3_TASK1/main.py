def make_multiplier(n):
    return lambda x: x * n
mult_by_3 = make_multiplier(3)
result = list(map(mult_by_3, filter(lambda x: x % 3 == 0, range(10))))
print(result)

def create_functions():
    return [lambda x: x + i for i in range(5)]
functions = create_functions()


result = [f(10) for f in functions]
print(result)