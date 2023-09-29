

def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D array (family), and returns a truncated version
    based on the provided start and end arguments.
    """
    if not isinstance(family, list):
        raise ValueError("The family parameter should be a list.")

    rows = len(family)

    # Check if all rows are lists and have the same number of columns
    if not all(isinstance(row, list) for row in family):
        raise ValueError("All elements of the 2D array should be lists.")

    columns = len(family[0])

    if not all(len(row) == columns for row in family[1:]):
        raise ValueError("All rows should have the same length.")

    # Print the original shape
    print(f"My shape is : ({rows}, {columns})")

    # Slice the list
    sliced_family = family[start:end]
    # Get the shape of the sliced list
    new_rows = len(sliced_family)
    new_columns = len(sliced_family[0]) if new_rows > 0 else 0

    # Print the new shape
    print(f"My new shape is : ({new_rows}, {new_columns})")

    return sliced_family
