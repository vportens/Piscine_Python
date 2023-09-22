def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
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
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise ValueError("Tous les éléments de la liste 'bmi' "
                         "doivent être des int ou des float.")

    if not isinstance(limit, int):
        raise ValueError("'limit' doit être un int.")

    return [b < limit for b in bmi]
