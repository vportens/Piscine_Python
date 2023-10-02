from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):

    def __init__(self, first_name, is_alive=True):
        # Initialiser à partir de la classe Baratheon
        Baratheon.__init__(self, first_name, is_alive)
        self._eyes = self.eyes
        self._hairs = self.hairs

    # Initialisation de proprety pour redefinir attribution de eyes et hairs
    @property
    def eyes(self):
        return self._eyes

    @eyes.setter
    def eyes(self, value):
        self._eyes = value

    @property
    def hairs(self):
        return self._hairs

    @hairs.setter
    def hairs(self, value):
        self._hairs = value

    def set_eyes(self, value):
        self.eyes = value

    def set_hairs(self, value):
        self.hairs = value

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs
