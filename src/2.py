from collections import Counter
from operator import xor


def get_passwords(input_filepath):
    """
    parse input filepath into a list of tuples (policy, password)
    """

    passwords = []
    with open(input_filepath, "r") as f:
        for line in f:
            policy, password = line.strip().split(": ")
            passwords.append((policy, password))
    return passwords


def parse_policy(policy):
    """
    parse policy from str into tuple (number1, number2, letter)
    """

    limit, letter = policy.split(" ")
    limits = limit.split("-")
    return (int(limits[0]), int(limits[1]), letter)


def is_password_valid(policy, password):
    """
    check whether the given password meet policy (min limit, max limit, letter)
    """

    min_limit, max_limit, letter = policy
    counter = Counter(password)
    return counter[letter] >= min_limit and counter[letter] <= max_limit


def is_password_valid2(policy, password):
    """
    new policy in part2
    check whether the given password meet policy (position1, position2, letter)
    - position is 1-based index
    - exactly one of these positions must contain the given letter
    """
    pos1 = policy[0] - 1
    pos2 = policy[1] - 1
    letter = policy[2]

    return xor(password[pos1] == letter, password[pos2] == letter)


def part1(passwords):
    n = 0
    for raw_policy, password  in passwords:
        policy = parse_policy(raw_policy)
        if is_password_valid(policy, password):
            n += 1
    print(f"Number of valid passwords = {n}")


def part2(passwords):
    n = 0
    for raw_policy, password  in passwords:
        policy = parse_policy(raw_policy)
        if is_password_valid2(policy, password):
            n += 1
    print(f"Number of valid passwords = {n}")


def main(input_filepath):
    passwords = get_passwords(input_filepath)
    part1(passwords)
    part2(passwords)


if __name__ == "__main__":
    from sys import argv

    main(argv[1])
