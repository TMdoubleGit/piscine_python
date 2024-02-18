from S1E9 import Character


class Baratheon(Character):
    """
    Baratheon class that inherits from Character.
    It has the same attributes as its parent class,
    but also a few more, such as:
        - family_name (string, always set on Baratheon)
        - eyes (string, always set on brown)
        - hairs (string, always set on dark)
    It also has same methods as the Character class, added to
    the list below:
        - create_baratheon(): creates a new Baratheon object.
        - def __str__(self): returns a str presenting the object.
        - def __repr__(self): returns a str with the object's representation.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor for the Baratheon class.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """
        Sets is_alive to False.
        """
        super().die()

    @staticmethod
    def create_baratheon(first_name: str, is_alive: bool = True):
        """
        Creates a new Baratheon object.
        """
        return Baratheon(first_name, is_alive)

    def __str__(self):
        """
        returns a string presenting the object.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        returns a str with the object's representation.
        """
        return self.__str__()


class Lannister(Character):
    """
    Lannister class that inherits from Character.
    It has the same attributes as its parent class,
    but also a few more, such as:
        - family_name (string, always set on Lannister)
        - eyes (string, always set on blue)
        - hairs (string, always set on light)
    It also has same methods as the Character class, added to
    the list below:
        - create_lannister(): creates a new Lannister object.
        - def __str__(self): returns a str presenting the object.
        - def __repr__(self): returns a str with the object's representation.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor for the Lannister class.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """
        Sets is_alive to False.
        """
        super().die()

    @staticmethod
    def create_lannister(first_name: str, is_alive: bool = True):
        """
        Creates a new Lannister object.
        """
        return Lannister(first_name, is_alive)

    def __str__(self):
        """
        returns a string presenting the object.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        returns a str with the object's representation.
        """
        return self.__str__()
