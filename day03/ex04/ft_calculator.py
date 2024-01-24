class calculator:
    """
    Class calculator
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> float:
        """
        Function product dot
        """
        ret = sum(x*y for x, y in zip(V1, V2))
        print("Dot product is: ", ret)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> list[float]:
        """
        Function add vec
        """
        ret = [x+y for x, y in zip(V1, V2)]
        print("Add Vector is: ", ret)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> list[float]:
        """
        Function Sous vec
        """
        ret = [x-y for x, y in zip(V1, V2)]
        print("Sous Vector is: ", ret)
