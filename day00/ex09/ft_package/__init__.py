def count_in_list(a, b):
    """
    Count occurrences of an element in a list.

    Parameters:
    - a (list): List to search for the element.
    - b : Element to count. Must match types in `a`.

    Returns:
    - int: Number of occurrences of `b` in `a`.

    Raises:
    - TypeError: If `a` isn't a list or types in `a` and `b` mismatch.

    Examples:
    >>> count_in_list([1, 2, 3, 2, 2, 4], 2)
    3
    >>> count_in_list(["apple", "banana", "apple"], "apple")
    2
    """
    if not isinstance(a, list):
        raise TypeError("The first argument must be a list")
    if not all(isinstance(elem, type(b)) for elem in a):
        raise TypeError("All elements of the list and the second"
                        "argument must be of the same type")

    return a.count(b)
