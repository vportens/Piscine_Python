def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:

    """
    Calculate the BMI (Body Mass Index) for each pair of height-weight values
    provided.

    Parameters:
    - height (list[int | float]): A list containing heights in meters.
    - weight (list[int | float]): A list containing weights in kilograms.

    Returns:
    - list[int | float]: A list of computed BMI values.

    Raises:
    - ValueError: If the two lists do not have the same length.
    - ValueError: If any element in the lists is not an int or a float.
    - ValueError: If height or weight is less than or equal to 0.

    Examples:
    >>> give_bmi([1.8, 1.65], [70, 55])
    [21.604938271604937, 20.202020202020204]
    """
    if len(height) != len(weight):
        raise ValueError("Les listes 'height' et 'weight'"
                         " doivent avoir la même longueur.")

    bmi = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise ValueError("Tous les éléments des listes 'height' et "
                             "'weight'"
                             " doivent être des int ou des float.")
        if h <= 0 or w <= 0:
            raise ValueError("La taille et le poids doivent être des valeurs"
                             " positives.")
        bmi.append(w / (h ** 2))

    return [w / (h * h) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Determine whether each BMI value in the list is below a specified limit.

    Parameters:
    - bmi (list[int | float]): A list of BMI values.
    - limit (int): The BMI limit to compare against.

    Returns:
    - list[bool]: A list of booleans indicating whether each BMI value is
                  below the 'limit'.

    Raises:
    - ValueError: If any element in the 'bmi' list is not an int or a float.
    - ValueError: If 'limit' is not an int.

    Examples:
    >>> apply_limit([21.6, 20.2], 21)
    [False, True]
    """
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise ValueError("Tous les éléments de la liste 'bmi' "
                         "doivent être des int ou des float.")

    if not isinstance(limit, int):
        raise ValueError("'limit' doit être un int.")

    return [b < limit for b in bmi]
