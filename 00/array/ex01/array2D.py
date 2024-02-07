import numpy as np

def slice_me(family: list, start: int, end:int) -> list:
    """
    This function takes a 2D array and returns a slice of the array from start to end.
    """
    try:
        assert isinstance(family, list), "AssertionError: family is not a list"
        assert isinstance(start, int), "AssertionError: start is not an integer"
        assert isinstance(end, int), "AssertionError: end is not an integer"
        assert start >= 0, "AssertionError: start is less than 0"
        assert abs(end) <= len(family), "AssertionError: end is greater than the length of family"
        assert family, "AssertionError: family is empty"
        assert all(len(item) == len(family[0]) for item in family), "AssertionError: family is not a 2D array"

        rows = len(family)
        columns = len(family[0])
        print("My shape is : (", rows, ", ", columns, ")")
        if (end >= 0):
            if (end > start):
                print("My new shape is : (",end - start, ", ", columns, ")")
                res = family[start:end]
            elif (end <= start):
                print("My new shape is : empty")
                res = []
        else:
            print("My new shape is : ( 1 ,", columns, " )")
            res = family[start]

        return res

    except AssertionError as e:
        print(e)
        print("Returning the original array")
        return family
