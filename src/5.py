def get_boarding_passes(input_filepath):
    """
    parse input filepath into list of boarding passes
    """
    boarding_passes = []
    with open(input_filepath, "r") as f:
        for line in f:
            boarding_passes.append(line.strip())
    return boarding_passes


def get_seat(boarding_pass):
    """
    given boarding pass code
    locate the seat in the form of (row, column, id)
    """

    n_rows = 128
    start_row = 0
    end_row = n_rows - 1

    # get rows
    for i in range(7):
        if boarding_pass[i] == "F":
            end_row = (end_row - start_row) // 2 + start_row
        else:
            # B
            start_row = end_row - ((end_row - start_row) // 2)

    n_cols = 8
    start_col = 0
    end_col = n_cols - 1

    # get column
    for i in range(7, len(boarding_pass)):
        if boarding_pass[i] == "L":
            end_col = (end_col - start_col) // 2 + start_col
        else:
            # B
            start_col = end_col - ((end_col - start_col) // 2)

    return start_row, start_col, start_row * 8 + start_col


def part1(boarding_passes):
    highest_id = 0
    for boarding_pass in boarding_passes:
        row, col, id_ = get_seat(boarding_pass)
        if id_ > highest_id:
            highest_id = id_
    print(f"highest id = {highest_id}")


def part2(boarding_passes):
    n_seats = 128 * 8

    nearby_seats = set()
    for boarding_pass in boarding_passes:
        row, col, id_ = get_seat(boarding_pass)
        nearby_seats.add(id_)

    min_seat_id = min(nearby_seats)
    max_seat_id = max(nearby_seats)
    all_seats = set([i for i in range(min_seat_id, max_seat_id + 1)])
    my_seat_id = list(all_seats - nearby_seats)[0]
    print(f"my seat id = {my_seat_id}")


def main(input_filepath):
    boarding_passes = get_boarding_passes(input_filepath)
    part1(boarding_passes)
    part2(boarding_passes)


if __name__ == "__main__":
    from sys import argv

    main(argv[1])
