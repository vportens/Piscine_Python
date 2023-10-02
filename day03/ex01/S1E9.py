from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract class for a character.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Constructor call for Character class.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Method die turn Character from alive to Dead.
        """
        pass


class Stark(Character):
    """
    Class Stark that herit from Character.
    """

    def __init(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Method die turn Stark from alive to Dead.
        """
        self.is_alive = False
