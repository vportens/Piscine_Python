import random
import string
from dataclasses import dataclass, field


def generate_id():
    """
    Genereate a random Id (15 letter in lowercase)
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Class student take to params :
    - name (str)
    - surname (str)

    Class have 3 other params that self init :
    - active (bool == true)
    - id (str randomgenerated)
    - login (first letter of name + 7 letter of surname)

    Use of field to set what need to be init or not
    """
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True, init=False)
    id: str = field(default_factory=generate_id, init=False)
    login: str = field(init=False)

    def __post_init__(self):
        """
        instantanement apres l'init va executer cela
        Combine le premier caractère de chaine1 avec jusqu'aux
        6 premiers caractères de chaine2.

        Args:
        chaine1 (str): La première chaîne de caractères.
        chaine2 (str): La seconde chaîne de caractères.

        Returns:
        str: La chaîne de caractères combinée.
        """
        if self.name:
            first_part = self.name[0].capitalize()
        else:
            first_part = ""
        second_part = self.surname[:7].lower()
        self.login = first_part + second_part
