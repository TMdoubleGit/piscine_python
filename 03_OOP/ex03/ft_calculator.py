class calculator:
    """
    This class is able to do calculations (addition,
    multiplication, substraction, division) of vector with a
    scalar.
    It has four methods, one for each operation described above.
    """
    def __init__(self, vector: list):
        """
        Constructor of the calculator class.
        """
        if not isinstance(vector, list):
            raise TypeError("vector must be a list")
        if not all(isinstance(x, (int, float)) for x in vector):
            raise TypeError("vector must contain only intergers and floats")
        self.vector = vector

    def __add__(self, object) -> None:
        """
        Addition method
        """
        if not isinstance(object, (int, float)):
            raise TypeError("object must be an integer or a float")
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """
        Multiplication method
        """
        if not isinstance(object, (int, float)):
            raise TypeError("object must be an integer or a float")
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """
        Substraction method
        """
        if not isinstance(object, (int, float)):
            raise TypeError("object must be an integer or a float")
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        if not isinstance(object, (int, float)):
            raise TypeError("object must be an integer or a float")
        if object == 0:
            raise ZeroDivisionError("division by 0")
        self.vector = [x / object for x in self.vector]
        print(self.vector)
