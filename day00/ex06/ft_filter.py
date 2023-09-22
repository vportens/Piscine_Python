def ft_filter(func, iterable):
    """
    Recreate the built-in filter function.

    Parameters:
    - func: The function to apply to each item.
    - iterable: The iterable to filter.

    Returns:
    A generator yielding filtered items.
    """
    return (item for item in iterable if func(item))
