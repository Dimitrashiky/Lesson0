def divide(first, second):
    from math import inf
    try:
        return first / second
    except ZeroDivisionError:
        return inf
