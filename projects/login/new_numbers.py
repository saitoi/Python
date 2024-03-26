from operator import add, sub, mul, truediv


operators = {'plus': add, 'minus': sub, 'times': mul, 'divided_by': truediv}


def create_number_func(value):
    return lambda func=None: value if not func else func(value)
def create_operator_func(value):
    return lambda func=None: operators[]

for i, name in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
    globals()[name] = create_number_func(i)

for key, value in operators:
    globals()[key] = create_operator_func()

def plus(y):
    return lambda x: operators['plus'](x, y)

def minus(y):
    return lambda x: operators['minus'](x, y)
def times(y):
    return lambda x: operators['times'](x, y)
def divided_by(y):
    return lambda x: operators['divided_by'](x, y)

# Exemplo de uso
print(nine(plus(one())))  # Deve retornar 10
