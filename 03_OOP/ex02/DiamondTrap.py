from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    King class that inherits from both Baratheon and
    Lannister class.
    It has the same attributes as its parents class, but two
    new methods are added to sets the King's eyes and hairs colours:
        - set_eyes(str).
        - set_hairs(str)
    It also have two getters to retrieve the value of these attributes.
    The King's class primarily inherits from the attribute values of
    the Baratheon class.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor for the King class.
        """
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """
        Returns eyes' attribute.
        """
        return self.eyes

    def get_hairs(self):
        """
        Returns hairs' attribute.
        """
        return self.hairs

    def set_eyes(self, colour: str):
        """
        Sets eyes' colour.
        """
        self.eyes = colour

    def set_hairs(self, colour: str):
        """
        Sets hairs' colour.
        """
        self.hairs = colour
