from give_bmi import give_bmi, apply_limit
from tqdm import tqdm
import time


def rgb_to_ansi(red, green, blue):
    return f"\033[38;2;{red};{green};{blue}m"


def main():
    # Create test cases here: differents lists with corrupted data in the list
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
    height1 = [1.80, 1.64, 2.06, 1.75, 1.69, 1.79, 1.78, 1.94]
    weight1 = [80.0, 65.0, 90.0, 70.0, 60.0, 75.0, 70.3, 85.5]
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    tests = [(test1, test11), (test2, test22), (test3, test33),
             (test4, test44), (test5, test55), (height, weight),
             (height1, weight1)]
    results = []
    FEDERATION_COLOR = (75, 115, 210)

    color = rgb_to_ansi(*FEDERATION_COLOR)
    for h, w in tqdm(tests, desc="Processing tests", unit="test",
                     bar_format=f"{color}{{bar}}\033[0m"):
        time.sleep(0.5)  # Decoration purpose
        try:
            results.append(give_bmi(h, w))
        except ValueError as e:
            results.append(str(e))
    for i, result in enumerate(results):
        print(f"Test {i}: {result}")
        if isinstance(result,
                      list) and all(isinstance(x, (int,
                                                   float)) for x in result):
            limit_applied = apply_limit(result, 30)
            print(f"Apply Limit for Test {i}: {limit_applied}")
            if all(limit_applied):
                print("Nobody is overweight")
            else:
                print("Somebody is overweight oupsy")
    
    print("test print doc")
    print(give_bmi.__doc__)


if __name__ == "__main__":
    main()
