import os
from collections import defaultdict

import numpy as np

os.chdir(os.path.dirname(__file__))


def get_lines(file_path, verbose=True):
    with open(file_path) as f:
        lines = f.readlines()
    print(f"Found {len(lines)} lines in {file_path.split('/')[-1]}")
    return lines


def next_pos(pos, width, right=3, down=1):
    return pos[0] + down, (pos[1] + right) % width


def count_trees(puzzle, slope, verbose=False):
    M = np.copy(puzzle)
    pos = (0, 0)
    trees = 0
    while pos[0] < len(lines):
        if M[pos] == "#":
            trees += 1
        if verbose:
            M[pos] = "X" if M[pos] == "#" else "O"
        pos = next_pos(pos, len(M[0]), right=slope[0], down=slope[1])
    if verbose:
        print(M)
        print(f"Encountered {trees} trees")
    return trees


lines = get_lines("./input.txt")
lines = [list(line) for line in lines]
for line in lines:
    if "\n" in line:
        line.remove("\n")
M = np.array([[char for char in line] for line in lines])

slope_labels = [
    "Right 1, down 1",
    "Right 3, down 1",
    "Right 5, down 1",
    "Right 7, down 1",
    "Right 1, down 2",
]

trees_count = defaultdict(int)
for label in slope_labels:
    slope = int(label.split()[1][0]), int(label.split()[-1])
    trees_count[label] = count_trees(M, slope)

print()
mul = 1
for k, v in trees_count.items():
    print(f"With slope '{k}': encountered {v} trees")
    mul = mul * v

print("All trees mul =", mul)
