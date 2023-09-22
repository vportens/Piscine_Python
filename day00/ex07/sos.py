import sys


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
    "E": ". ", "F": "..-. ", "G": "--. ",
    "H": ".... ", "I": ".. ", "J": ".--- ", "K": "-.- ",
    "L": ".-.. ", "M": "-- ", "N": "-. ",
    "O": "--- ", "P": ".--. ", "Q": "--.- ", "R": ".-. ",
    "S": "... ", "T": "- ", "U": "..- ",
    "V": "...- ", "W": ".-- ", "X": "-..- ", "Y": "-.-- ", "Z": "--.. ",
    "1": ".---- ", "2": "..--- ", "3": "...-- ", "4": "....- ", "5": "..... ",
    "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. ", "0": "----- "
}


def to_morse(chaine):
    morse_translated_str = ''.join(
        NESTED_MORSE[char.upper()] for char in chaine)
    return morse_translated_str[:-1]


def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError("the arguments are bad")

        chaine = sys.argv[1]
        if not all(c.isalpha() or c.isspace() or c.isnumeric for c in chaine):
            raise ValueError("the arguments are bad")

        result = to_morse(chaine)
        print(result)

    except ValueError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
