import sys


def filtrer_mots(chaine, n):
    """
    Renvoie une liste de mots de la chaîne qui ont une longueur supérieure à n.

    Parameters:
    - chaine: La chaîne à filtrer.
    - n: L'entier indiquant la longueur minimale des mots à inclure.

    Returns:
    Une liste de mots filtrés.
    """
    return [mot for mot in chaine.split() if (lambda x: len(x) > n)(mot)]


def main():

    try:
        if len(sys.argv) != 3:
            raise ValueError("the arguments are bad")
        try:
            n = int(sys.argv[2])
            chaine = sys.argv[1]
        except ValueError:
            raise ValueError("the arguments are bad")

        if not all(c.isalpha() or c.isspace() for c in chaine):
            raise ValueError("the arguments are bad")

        result = filtrer_mots(chaine, n)
        print(result)
    except ValueError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
