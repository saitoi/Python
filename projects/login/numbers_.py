from operator import add, sub, mul, floordiv

num_str = ['zero', 'one', 'two', 'three', 'four',
           'five', 'six', 'seven', 'eight', 'nine',
           'plus', 'minus', 'times', 'divided_by']

operators = {'plus': add, 'minus': sub, 'times': mul, 'divided_by': floordiv}
symbols = {num: index for index, num in enumerate(num_str)}

symbols.update(operators)

ret_item = lambda string, lst: next((item for item in lst if item in string), None)
ret_bool = lambda string, lst: (True for item in lst if item in string else False)


def numbers(name=''):
    if name and ret_item(list(operators.keys())):
        expression = numbers.__name__.join(name)
        operation = ret_item(expression, operators)
        final_expr = expression.split(operation)
        return symbols[operation](symbols[final_expr[0], symbols[final_expr[1]]])
    else:
        return name+numbers.__name__


for name in num_str:
    globals()[name] = numbers(name)

print(nine())  # This will print the number associated with 'nine' in the symbols dictionary
