import os
from itertools import combinations

import numpy as np

os.chdir(os.path.dirname(__file__))


def get_lines(file_path, verbose=True):
    with open(file_path) as f:
        lines = f.readlines()
    print(f"Found {len(lines)} lines in {file_path.split('/')[-1]}")
    return lines


def get_block_between_blanklines(file_path, verbose=True):
    with open(file_path) as f:
        all_lines = f.read().strip()
    blocks = all_lines.split("\n\n")
    print(f"Found {len(blocks)} blocks in {file_path.split('/')[-1]}")
    return blocks


def matrix_from_lines(lines):
    lines = [list(line) for line in lines]
    for line in lines:
        if "\n" in line:
            line.remove("\n")
    M = np.array([[char for char in line] for line in lines])
    return M


input_file = "input.txt"
lines = get_lines(input_file)
numbers = np.array(sorted([int(line) for line in lines]))

diff = np.array([numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)])
counts = np.array(np.unique(diff, return_counts=True)[1]) + 1
print(f"Product of 1-jolt and 3-jolt differences is {'*'.join([str(x) for x in counts])}={counts.prod()}")

numbers = np.array([0] + list(numbers))
diff = np.array([numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)])
subsets = np.split(numbers, np.where(diff == 3)[0] + 1)
print(f"\n{subsets=}")


def comb(subset):
    return sum([sum(1 for ignore in combinations(subset, r)) for r in range(max(0, len(subset) - 2), len(subset) + 1)])


nb_arrangements = np.array([comb(subset[1:-1]) for subset in subsets if len(subset) > 2]).prod()
print(f"\n\t{nb_arrangements=}")
