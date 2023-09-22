def count_in_list(a, b):
    if not isinstance(a, list):
        raise TypeError("The first argument must be a list")
    if not all(isinstance(elem, type(b)) for elem in a):
        raise TypeError("All elements of the list and the second"
                        "argument must be of the same type")

    return a.count(b)
