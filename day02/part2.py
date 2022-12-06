import os
import argparse

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input.txt")

# A = Rock
# B = Paper
# C = Scissors
# Rock > Scissors > Paper > Rock

# X = lose
# Y = draw
# Z = win

get_shape_to_win_against = {
    "B": "A",
    "C": "B",
    "A": "C"
}

get_shape_to_lose_against = {
    "A": "B",
    "B": "C",
    "C": "A"
}


def points_of_shape(shape):
    return ord(shape) - ord("A") + 1


def compute(input):
    total_score = 0
    for value in input:
        opponent_shape, match_result = value.strip().split(" ")

        my_shape = None
        if match_result == "X":
            my_shape = get_shape_to_win_against[opponent_shape]
        elif match_result == "Y":
            my_shape = opponent_shape
            total_score += 3
        elif match_result == "Z":
            my_shape = get_shape_to_lose_against[opponent_shape]
            total_score += 6

        total_score += points_of_shape(my_shape)

    return total_score


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_FILE)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.readlines()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
