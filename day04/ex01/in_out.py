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
 
def outer(x:int | float, function):
    count = 0

    def inner():
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
    

def main():
    try:
        my_counter = outer(3, square)
        print(my_counter()) 
        print(my_counter())
        print(my_counter())
        print("---")
        another_counter = outer(1.5, pow)
        print(another_counter())
        print(another_counter())
        print(another_counter())
        test_maxint = outer(350000, square)
        print(test_maxint())
        print(test_maxint())
        print(test_maxint())
        print(test_maxint())
        print(test_maxint())
        print(test_maxint())
        print(test_maxint())
        print(test_maxint())
        print(test_maxint())
        print(test_maxint())
    except Exception as e:
        print(e)
    
if __name__ == "__main__":
    main()