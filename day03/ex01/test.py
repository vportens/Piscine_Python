from S1E9 import Character, Stark
from S1E7 import Baratheon, Lannister

Ned = Stark("Ned")

print(Ned.__dict__)
print(Ned.is_alive)

Ned.die()

print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)

print("---")

Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)

print("--- ex01 test")

Robert = Baratheon("Robert")

print(Robert.__dict__)
print(Robert.__str__)
print(Robert.__repr__)
print(Robert.is_alive)

Robert.die()
print(Robert.is_alive)

print(Robert.__doc__)

print("---")
Cersei = Lannister("Cersei")

print(Cersei.__dict__)
print(Cersei.__str__)
print(Cersei.is_alive)

print("---")
Jaine = Lannister.create_lannister("Jaine", True)
print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")


print("---")