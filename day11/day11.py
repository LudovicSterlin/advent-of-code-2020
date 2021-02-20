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


def count_occupied_adjacent(M, i, j):
    count = 0
    for i_ in range(i - 1, i + 2):
        for j_ in range(j - 1, j + 2):
            if (i_, j_) != (i, j) and i_ >= 0 and i_ < M.shape[0] and j_ >= 0 and j_ < M.shape[1] and M[i_, j_] == "#":
                count += 1
    return count


def count_occupied(M):
    return (M == "#").sum()


input_file = "input.txt"
lines = get_lines(input_file)
M = matrix_from_lines(lines)

nb_occupied = count_occupied(M)

newM = M.copy()
new_nb_occupied = -1
while nb_occupied != new_nb_occupied:
    newM = M.copy()
    nb_occupied = new_nb_occupied
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if M[i, j] == "L" and count_occupied_adjacent(M, i, j) == 0:
                newM[i, j] = "#"
            if M[i, j] == "#" and count_occupied_adjacent(M, i, j) > 3:
                newM[i, j] = "L"
    new_nb_occupied = count_occupied(newM)
    M = newM

print(newM)
print(count_occupied(newM))
# nb_arrangements = np.array([comb(subset[1:-1]) for subset in subsets if len(subset) > 2]).prod()
# print(f"\n\t{nb_arrangements=}")
