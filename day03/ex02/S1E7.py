from S1E9 import Character


class Baratheon(Character):
    """
    Class Baratheon
    Constructeur attribut:
    - first_name : str
    - is_alive : bool, optional (True by default)
    """
    def __init__(self, first_name, is_alive=True):
        """
        Init with first_name and is_alive
        Attributes add :
        - Eyes = Brown
        - Hairs = Dark
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        """
        Doc __str__
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """
        Doc __repr__
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """
        Change status of is_alive to false
        """
        self.is_alive = False


class Lannister(Character):
    """
    Class Lannister
    Constructeur attribut:
    - first_name : str
    - is_alive : bool, optional (True by default)
    """

    def __init__(self, first_name, is_alive=True):
        """
        Init with first_name and is_alive
        Attributes add :
        - Eyes = Bleu
        - Hairs = Light
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """
        Doc __str__
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Doc __repr__
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        Create and return a new lannister obj
        """
        return cls(first_name, is_alive)

    def die(self):
        """
        Change is_alive to false
        """
        self.is_alive = False
