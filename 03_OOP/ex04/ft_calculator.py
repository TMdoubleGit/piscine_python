class calculator:
    """
    This class is able to do calculations (dot product,
    addition and substraction) of two vectors with a
    scalar.
    It has three methods, one for each operation described above.
    """
    @staticmethod
    def dotproduct(v1: list[float], v2: list[float]) -> None:
        """
        Prints the product of two vectors.
        """
        if not isinstance(v1, list) or not isinstance(v2, list):
            raise TypeError("both vectors must be lists")
        if len(v1) != len(v2):
            raise ValueError("vectors must be the same size")
        print("Dot product is :", sum([x * y for x, y in zip(v1, v2)]))

    @staticmethod
    def add_vec(v1: list[float], v2: list[float]) -> None:
        """
        Prints the addition of two vectors.
        """
        if not isinstance(v1, list) or not isinstance(v2, list):
            raise TypeError("both vectors must be lists")
        if len(v1) != len(v2):
            raise ValueError("vectors must be the same size")
        print("Add vector is :", [float(x + y) for x, y in zip(v1, v2)])

    @staticmethod
    def sous_vec(v1: list[float], v2: list[float]) -> None:
        """
        Prints the substraction of two vectors.
        """
        if not isinstance(v1, list) or not isinstance(v2, list):
            raise TypeError("both vectors must be lists")
        if len(v1) != len(v2):
            raise ValueError("vectors must be the same size")
        print("Sous vector is :", [float(x - y) for x, y in zip(v1, v2)])
