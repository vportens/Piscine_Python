import random
import string
from dataclasses import dataclass, field

def generate_id():
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    name: str
    nickname: str
    active: bool = True
    id: str = generate_id()
    login: str = genereate_login()