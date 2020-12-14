import os

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
numbers = [int(line) for line in lines]


def get_comb(values):
    possibilities = set()
    for i in range(len(values) - 1):
        for j in range(i + 1, len(values)):
            possibilities.add(values[i] + values[j])
    return possibilities


def check_XMAS(numbers, ind, n_behind=5):
    valids = get_comb(numbers[ind - n_behind : ind])
    return numbers[ind] in valids


n_behind = 25 if input_file == "input.txt" else 5
num_index = n_behind
while check_XMAS(numbers, num_index, n_behind):
    num_index += 1

invalid_number = numbers[num_index]
print(f"The first invalid number is {invalid_number}, at index {num_index}")

found = False
start = 0
end = 1
while not found:
    my_sum = sum(numbers[start : end + 1])
    if my_sum == invalid_number:
        found = True
        break
    if my_sum < invalid_number:
        end += 1
    if my_sum > invalid_number:
        start += 1
        end = start + 1

print(start, end, found)
print(f"Found contiguous set. from index {start} to {end}")
contiguous_set = numbers[start : end + 1]
print(f"{contiguous_set=}")
smallest, largest = min(contiguous_set), max(contiguous_set)
print(f"Smallest is {smallest}, largest is {largest}")
print(f"\t encryption weakness is {smallest+largest}")
