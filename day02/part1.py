import os
import argparse

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input.txt")

# A = Rock
# B = Paper
# C = Scissors

# X = Rock
# Y = Paper
# Z = Scissors
# Rock > Scissors > Paper > Rock

my_shape_scores = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

win = [
    ("A", "Y"),
    ("B", "Z"),
    ("C", "X")
]


def compute(input):
    total_score = 0
    for value in input:
        opponent_shape, my_shape = value.strip().split(" ")

        if opponent_shape == chr((ord(my_shape) - 23)):
            total_score += 3
        elif win.count((opponent_shape, my_shape)) > 0:
            total_score += 6

        total_score += my_shape_scores[my_shape]

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
