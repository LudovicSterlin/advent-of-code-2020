import os
from collections import defaultdict

import numpy as np

os.chdir(os.path.dirname(__file__))


def get_lines(file_path, verbose=True):
    with open(file_path) as f:
        lines = f.readlines()
    print(f"Found {len(lines)} lines in {file_path.split('/')[-1]}")
    return lines


def get_block_between_blanklines(file_path, verbose=True):
    with open(file_path) as f:
        all_lines = f.read()
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


def found_seat(b_pass, nrows=128, ncols=8):
    rows = list(range(nrows))
    cols = list(range(ncols))
    row_indics = b_pass[:7]
    col_indics = b_pass[7:]
    for token in row_indics:
        if token == "F":
            rows = rows[: len(rows) // 2]
        elif token == "B":
            rows = rows[len(rows) // 2 :]
    for token in col_indics:
        if token == "L":
            cols = cols[: len(cols) // 2]
        elif token == "R":
            cols = cols[len(cols) // 2 :]
    row, column, seat_id = rows[0], cols[0], rows[0] * 8 + cols[0]
    return row, column, seat_id


lines = get_lines("./input.txt")
passes = [list(line) for line in lines]
for b_pass in passes:
    if "\n" in b_pass:
        b_pass.remove("\n")

pass_dict = defaultdict(list)
for b_pass in passes:
    row, column, seat_id = found_seat(b_pass)
    # print(b_pass, row, column, seat_id)
    pass_dict["row"].append(row)
    pass_dict["column"].append(column)
    pass_dict["seat_id"].append(seat_id)

print(f"\nHigher seat id is {max(pass_dict['seat_id'])}")

seat_ids = sorted(pass_dict["seat_id"])
target = np.arange(seat_ids[0], seat_ids[-1])
my_seat = np.setdiff1d(target, seat_ids)
print(f"Missing seat is {my_seat}, so it's my seat")
