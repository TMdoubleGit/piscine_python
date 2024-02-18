def square(x: int | float) -> int | float:
    """
    This function returns the square of an argument.
    """
    return (x ** 2)


def pow(x: int | float) -> int | float:
    """
    This function returns the exponentiation of the argument by himself.
    """
    return (x ** x)


def outer(x: int | float, function) -> object:
    """
    This function returns an object that when called returns the results
    of the arguments calculation.
    """
    count = 0

    def inner() -> float:
        nonlocal count, x
        if count == 0:
            count = x
        count = function(count)
        return (count)

    return (inner)
