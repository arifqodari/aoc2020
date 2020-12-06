def get_map(input_filepath):
    """
    parse input filepath into a map (list of patters)
    """

    map_ = []
    with open(input_filepath, "r") as f:
        for line in f:
            map_.append(line.strip())
    return map_


def part1(map_):
    print("=" * 10 + " Part 1 " + "=" * 25)

    # slope is right 3 down 1
    # so we only process column at index 3, 6, ...
    # and row starting at index 1, 2, ...
    n_trees = 0
    for i in range(1, len(map_)):
        line = map_[i]

        # get column index
        col = i * 3
        if col >= len(line):
            col = col % len(line)

        # get marker 
        if line[col] == "#":
            n_trees += 1

    print(f"number of trees = {n_trees}")


def part2(map_):
    print("\n" + "=" * 10 + " Part 2 " + "=" * 25)

    # there are multiple slopes
    # we need to recompute step for the iteration and column index
    # for each slope

    # slope is tuple (right, down)
    slopes = [
            (1, 1),
            (3, 1),
            (5, 1),
            (7, 1),
            (1, 2)
            ]

    prod_n_trees = 1

    for slope in slopes:
        start = slope[1]
        step = slope[1]
        n_trees = 0

        for row, i in enumerate(range(start, len(map_), step)):
            line = map_[i]

            # get column index
            col = (row + 1) * slope[0]
            if col >= len(line):
                col = col % len(line)

            # get marker
            if line[col] == "#":
                n_trees += 1

        print(f"number of trees = {n_trees}")
        prod_n_trees *= n_trees
    print(f"product of number of trees = {prod_n_trees}")


def main(input_filepath):
    map_ = get_map(input_filepath)
    part1(map_)
    part2(map_)


if __name__ == "__main__":
    from sys import argv

    main(argv[1])
