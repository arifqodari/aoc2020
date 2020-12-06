from collections import Counter


def get_answers(input_filepath):
    """
    parse input filepath into list of answers
    each group's answers is separated by blank line
    each person's answers is written in individual line
    """

    answers = []
    with open(input_filepath, "r") as f:
        group = []
        for line in f:
            line = line.strip()

            # if found blank line, put previous group into the list
            if line == "":
                answers.append(group)
                group = []
            else:
                group.append(line)

        # append the last group
        answers.append(group)
    return answers


def part1(answers):
    """
    answers is list of list answers
    """

    n_yes = []
    for group in answers:
        c = Counter()
        for person in group:
            c.update(person)
        n_yes.append(len(c.keys()))

    sum_yes = sum(n_yes)
    print(f"Sum of yes = {sum_yes}")


def part2(answers):
    """
    answers is list of list answers
    """

    n_yes = []
    for group in answers:
        group_questions = []
        for person in group:
            group_questions.append(set(person))
        common_questions = set.intersection(*group_questions)
        n_yes.append(len(common_questions))

    sum_yes = sum(n_yes)
    print(f"Sum of yes = {sum_yes}")


def main(input_filepath):
    answers = get_answers(input_filepath)
    part1(answers)
    part2(answers)


if __name__ == "__main__":
    from sys import argv

    main(argv[1])
