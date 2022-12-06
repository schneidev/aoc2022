import os
import argparse

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input.txt")


def get_priority(item):
    base = ord("a") - 1 if item.islower() else ord("A") - 27
    return ord(item) - base


def compute(input):
    sum_of_priorities = 0
    it = iter(input)
    for i in range(0, len(input), 3):
        backpack1 = set(input[i].strip())
        backpack2 = set(input[i+1].strip())
        backpack3 = set(input[i+2].strip())

        shared_items = backpack1.intersection(
            backpack2).intersection(backpack3)
        for shared_item in shared_items:
            sum_of_priorities += get_priority(shared_item)

    return sum_of_priorities


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_FILE)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.readlines()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
