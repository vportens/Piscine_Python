from ft_package import count_in_list


def main():
    print("test de la fonction que nous avons"
          "créé dans notre propre librairie")
    try:
        print(count_in_list([1, 2, 3, 4, 5], 3))
        print(count_in_list([1, 2, 3, 4, 5], 6))
        print(count_in_list([1, 2, 3, 4, 5], 'a'))

    except TypeError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
