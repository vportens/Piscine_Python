def square(x: int | float):
    """
    Return the square of x.
    """
    ret = 0
    try:
        ret = x ** 2
        return ret
    except Exception as e:
        print(e)
        return ret


def pow(x: int | float):
    """
    Return the exponential of x by x.
    """
    ret = 0
    try:
        ret = x ** x
        return ret
    except Exception as e:
        print(e)
        return ret


def outer(x: int | float, function):

    """
    Returns a closure that takes no arguments and applies
    the given function to the input value.

    Parameters:
    x (int | float): The input value.
    function (callable): The function to be applied to the input value.

    Returns:
    callable: A closure that applies the given function to the
    input value and returns the result.
    """
    count = 0

    def inner():
        """
        Applies the given function to the input value and returns the result.

        Returns:
        int | float: The result of applying the function to the input value.
        """
        nonlocal count
        nonlocal x
        count += 1
        try:
            x = function(x)
            return x
        except Exception as e:
            print(e)
            return 0

    return inner
