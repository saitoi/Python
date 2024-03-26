def print_backwards(*args, end='', **kwargs):
    print(kwargs)
    print(*args[::-1], end=end, **kwargs)


def backwards_print(*args, **kwargs):
    sep_char = kwargs.pop('sep', ' ')
    print(sep_char.join(word[::-1] for word in args[::-1]), **kwargs)


backwards_print("hello", "planet", "earth", end='.')
