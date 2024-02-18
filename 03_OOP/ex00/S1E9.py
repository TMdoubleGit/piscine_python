from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract class "Character" with two attributes:
        - first_name (string)
        - is_alive (bool, non mandatory, set to True by default)
    It also has a method that switches is_alive from True to False.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor of the abstract class.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Sets is_alive to False.
        """
        self.is_alive = False


class Stark(Character):
    """
    Stark class that inherits from Character.
    It has the same methods and attributes as its parent class.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor of the Stark class.
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Sets is_alive to False.
        """
        super().die()
