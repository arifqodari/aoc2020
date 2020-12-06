from operator import mul
from functools import reduce
from itertools import combinations


def get_numbers(input_filepath):
    """
    get list of numbers
    """

    numbers = []
    with open(input_filepath, "r") as f:
        for line in f:
            number = int(line.strip())
            numbers.append(number)
    return numbers


def find_products(numbers, n):
    """
    calculate the product of n numbers that sum to 2020
    """

    for c in combinations(numbers, n):
        if sum(c) == 2020:
            prod = reduce(mul, c)
            print(f"multiply {c} = {prod}")


def main(input_filepath):
    numbers = get_numbers(input_filepath)
    find_products(numbers, 2)
    find_products(numbers, 3)


if __name__ == "__main__":
    from sys import argv

    main(argv[1])
