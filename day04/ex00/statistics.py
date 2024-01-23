import numpy as np


def ft_statistics(*args, **kwargs):
    """
    This function take a unknown number of arguments :
    - numbers
    - stings (Median, Mean, Quadrile, Standard deviation, Variance)
    Then print the result of calculation demanded by the arg used in the function.
    Exemple : 
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    """

    lst_authoris_operations = ["median", "mean", "quartile", "std", "var"]

    ## Check if args are numbers only
    lst_numbers = []
    for arg in args:
        if isinstance(arg, (int, float)):
            lst_numbers.append(arg)
        else:
            print(f"Error: {arg} is not allowed")
            print("Error: only numbers are allowed")
            return
    
    ## Check if kwargs
    lst_operations = []
    for key, value in kwargs.items():
        if value in lst_authoris_operations:
            lst_operations.append(value)
        else:
            print(f"Error: {value} is not allowed")
            print("Error: only median, mean, quartile, std and var are allowed")
            return
    
    for operation in lst_operations:
        if (len(lst_numbers)) == 0:
            print("ERROR")
        elif operation == "median":
            print(f"median : {np.median(lst_numbers)}")
        elif operation == "mean":
            print(f"mean : {np.mean(lst_numbers)}")
        elif operation == "quartile":
            quadrile = np.percentile(lst_numbers, [25, 75])
         #   print(f"quartile : {np.percentile(lst_numbers, [25, 75])}")
            print(f"quartile : [{quadrile[0]:.3f}, {quadrile[1]:.3f}]")
        elif operation == "std":
            print(f"std : {np.std(lst_numbers)}")
        elif operation == "var":
            print(f"variance : {np.var(lst_numbers)}")
        else:
            print("Error: something went wrong")



def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    #ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile", titi="std", tuti="var")
    ft_statistics(3,32.32, 432432, 434.2222, ubabab="ttt")
    ft_statistics(3,32.32, 432432, 434.2222, ubabab="mean")
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")

if __name__ == "__main__":
    main()
    