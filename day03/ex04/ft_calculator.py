from typing import List


class calculator:
    """
    Class calculator
    """
    @staticmethod
    def dotproduct(V1: List[float], V2: List[float]) -> float:
        """
        Function product dot
        """
        ret = sum(x*y for x, y in zip(V1, V2))
        print("Dot product is: ", ret)

    @staticmethod
    def add_vec(V1: List[float], V2: List[float]) -> List[float]:
        """
        Function add vec
        """
        ret = [x+y for x, y in zip(V1, V2)]
        print("Add Vector is: ", ret)

    @staticmethod
    def sous_vec(V1: List[float], V2: List[float]) -> List[float]:
        """
        Function Sous vec
        """
        ret = [x-y for x, y in zip(V1, V2)]
        print("Sous Vector is: ", ret)
