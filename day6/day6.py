import os
from functools import reduce

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


# Part1
print("\nPart 1")
groups = get_block_between_blanklines("./input.txt")
groups = [g.replace("\n", "") for g in groups]

unique_answers = [set(sorted(group)) for group in groups]
counts = [len(a) for a in unique_answers]

print(f"The sum of those counts is {sum(counts)}")


# Part2
print("\nPart 2")
groups = get_block_between_blanklines("./input.txt")
groups = [g.split("\n") for g in groups]
groups = [[list(g) for g in group] for group in groups]
print(groups[0])
everyone_yes = [reduce(np.intersect1d, group) for group in groups]
print(everyone_yes[0])

counts = [len(a) for a in everyone_yes]
# print(counts)
print(f"The sum of those counts is {sum(counts)}")
