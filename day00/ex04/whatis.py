import sys


def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def argChecker():
    s = sys.argv
    assert len(s) <= 2, "more than one argument is provided"
    if len(s) == 1:
        return
    assert is_integer(s[1]), "argument is not an integer"
    number = int(s[1])
    print("I'm Even.") if number % 2 == 0 else print("I'm Odd.")


try:
    argChecker()
except AssertionError as e:
    print(f"AssertionError: {e}")
