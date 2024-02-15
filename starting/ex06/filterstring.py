import sys
from ft_filter import ft_filter


def main():
    ac = len(sys.argv)
    try:
        assert ac == 3, "AssertionError: the arguments are bad"
        if not (sys.argv[1].__class__ == str and sys.argv[2].isdigit()):
            raise AssertionError("AssertionError: the arguments are bad")

        else:
            j = sum(not (c.isalpha() or c.isspace()) for c in sys.argv[1])
            if j > 0:
                raise AssertionError("AssertionError: the arguments are bad")

        max_len = int(sys.argv[2])

        initial_list = sys.argv[1].split()
        flambda = lambda s: len(s) > max_len
        filtered_list = ft_filter(flambda, initial_list)

        print(filtered_list)

    except AssertionError as e:
        print(e)


if (__name__ == "__main__"):
    main()
