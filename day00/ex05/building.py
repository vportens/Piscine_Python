import sys
import string


def compter_caracteres(texte):
    """
    Compte différents types de caractères dans une chaîne de caractères.

    La fonction analyse le texte fourni et affiche:
    - Nombre total de caractères.
    - Nombre de lettres majuscules.
    - Nombre de lettres minuscules.
    - Nombre de signes de ponctuation.
    - Nombre d'espaces.
    - Nombre de chiffres.

    Paramètres:
    - texte (str): Chaîne à analyser.

    Résultat:
    Affiche les compteurs pour chaque type de caractère.
    """
    upper_letters = sum(1 for char in texte if char.isupper())
    lower_letters = sum(1 for char in texte if char.islower())
    punctuation = sum(1 for char in texte if char in string.punctuation)
    punctuation_chars = set('!"#$%&\'()*+,-./:;<=>?@[\\]_^`{|}~')
    punctuation = sum(1 for char in texte if char in punctuation_chars)
    spaces = sum(1 for char in texte if char.isspace())
    digits = sum(1 for char in texte if char.isdigit())

    total_chars = len(texte)

    print(f"The text contains {total_chars} characters:")
    print(f"{upper_letters} upper letters")
    print(f"{lower_letters} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    if len(sys.argv) == 2:
        compter_caracteres(sys.argv[1])
    elif len(sys.argv) == 1:
        try:
            # Use readline() instead of input() to better handle the EOF
            # situation (Ctrl+D).
            print("What is the text to count?")
            texte = sys.stdin.readline()
            if not texte:  # Si l'utilisateur a juste fait Ctrl+D
                print("No input provided. Exiting.")
                return
            compter_caracteres(texte)
        except EOFError:  # Gère Ctrl+D
            print("No carriage return detected. Exiting.")
    else:
        raise AssertionError("Too many arguments provided!")


if __name__ == "__main__":
    main()
