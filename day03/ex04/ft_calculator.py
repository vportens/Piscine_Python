from typing import List


class calculator:

    @staticmethod
    def dotproduct(V1: List[float], V2: List[float]) -> float:
        ret = sum(x*y for x, y in zip(V1, V2))
        print("Dot product is: ", ret)

    @staticmethod
    def add_vec(V1: List[float], V2: List[float]) -> List[float]:
        ret = [x+y for x, y in zip(V1, V2)]
        print("Add Vector is: ", ret)

    @staticmethod
    def sous_vec(V1: List[float], V2: List[float]) -> List[float]:
        ret = [x-y for x, y in zip(V1, V2)]
        print("Sous Vector is: ", ret)
