from S1E9 import Character


class Baratheon(Character):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return f"Baratheon: {self.first_name}, living state: {self.is_alive}"

    def __repr__(self):
        return f"<Baratheon(name={self.first_name}, alive={self.is_alive})>"

    def die(self):
        self.is_alive = False


class Lannister(Character):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        return f"Lannister: {self.first_name}, living state: {self.is_alive}"

    def __repr__(self):
        return f"<Lannister(name={self.first_name}, alive={self.is_alive})>"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)

    def die(self):
        self.is_alive = False
