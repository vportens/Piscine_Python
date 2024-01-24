from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Class King take Baratheon and Lannister class
    """

    def __init__(self, first_name, is_alive=True):
        """
        Init from Baratheon class
        """
        # Initialiser à partir de la classe Baratheon
        Baratheon.__init__(self, first_name, is_alive)

    def set_eyes(self, eyes: str):
        """change the eyes attribute"""
        self.eyes = eyes

    def set_hairs(self, hairs: str):
        """change the hairs attribute"""
        self.hairs = hairs

    def get_eyes(self):
        """return the eyes attribute"""
        return self.eyes

    def get_hairs(self):
        """return the hairs attribute"""
        return self.hairs
