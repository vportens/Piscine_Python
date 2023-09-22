from give_bmi import give_bmi, apply_limit

# Create test cases here: differents lists with compt data in the list
test1 = [1, 'a', 3]
test11 = [1, 2, 3]
test2 = [1, 2, 3]
test22 = [1, 'a', 3]
test3 = ['tes', 'testd', 'teste']
test33 = ['tes', 'testd', 'teste']
test4 = [1, 2, 3]
test44 = ['fdjsk', 'fjdsk', 'fjdsk']
test5 = [1, 2, 3]
test55 = [1, 2]

try:
    print(give_bmi(test1, test11))
except ValueError as e:
    print(e)

try:
    print(give_bmi(test2, test22))
except ValueError as e:
    print(e)

try:
    print(give_bmi(test3, test33))
except ValueError as e:
    print(e)

try:
    print(give_bmi(test4, test44))
except ValueError as e:
    print(e)

try:
    print(give_bmi(test5, test55))
except ValueError as e:
    print(e)
# create multiple valide tests cases using list of int
# and float with the same length and positive values with different length

height1 = [1.80, 1.64, 2.06, 1.75, 1.69, 1.79, 1.78, 1.94]
weight1 = [80.0, 65.0, 90.0, 70.0, 60.0, 75.0, 70.3, 85.5]

height = [2.71, 1.15]
weight = [165.3, 38.4]

try:
    print("test de l'ecole")
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
except ValueError as e:
    print(e)

try:
    print("test perso")
    bmi = give_bmi(height1, weight1)
    print(bmi, type(bmi))

    lst = apply_limit(bmi, 30)
    if all(lst):
        print("Nobody is overweight")
    else:
        print("Somebody is overweight oupsy")


except ValueError as e:
    print(e)
