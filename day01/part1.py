import os
import argparse

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(input):
    elves = [0]
    i = 0
    for value in input:
        value = value.strip()

        if value == "":
            i += 1
            elves.append(0)
        else:
            elves[i] += int(value)

    return max(elves)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_FILE)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.readlines()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
