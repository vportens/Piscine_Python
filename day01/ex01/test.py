from array2D import slice_me
try: 
    family = [[1.80, 78.4],

                [2.15, 102.7, 115.3],
                [2.10, 98.5],
                [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

except Exception as e:
    print("An error occured: ", e)