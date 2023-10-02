class calculator:
    def __init__(self, vector):
        if not all(isinstance(i, (int, float)) for i in vector):
            raise ValueError("All elements of the vector should be numbers.")
        self.vector = vector

    def __add__(self, scalar):
        result = [x + scalar for x in self.vector]
        print(result)
        return calculator(result)

    def __mul__(self, scalar):
        result = [x * scalar for x in self.vector]
        print(result)
        return calculator(result)

    def __sub__(self, scalar):
        result = [x - scalar for x in self.vector]
        print(result)
        return calculator(result)

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        result = [x / scalar for x in self.vector]
        print(result)
        return calculator(result)
