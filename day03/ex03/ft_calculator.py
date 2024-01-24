class calculator:
    """
    Class calculator
    """
    def __init__(self, vector):
        """
        Init class
        """
        if not all(isinstance(i, (int, float)) for i in vector):
            raise ValueError("All elements of the vector should be numbers.")
        self.vector = vector

    def __add__(self, scalar):
        """"
        Add fonction for scalar
        """
        result = [x + scalar for x in self.vector]
        print(result)
        self.vector = result
        return calculator(result)

    def __mul__(self, scalar):
        """
        Multiplicatin for scalar
        """
        result = [x * scalar for x in self.vector]
        print(result)
        self.vector = result
        return calculator(result)

    def __sub__(self, scalar):
        """
        Sub fonction for scalar
        """
        result = [x - scalar for x in self.vector]
        print(result)
        self.vector = result
        return calculator(result)

    def __truediv__(self, scalar):
        """
        True div for scalar
        """
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        result = [x / scalar for x in self.vector]
        self.vector = result
        print(result)
        return calculator(result)
