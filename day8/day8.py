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


lines = get_lines("./input.txt")
instructions = [line.split(" ") for line in lines]
for ins in instructions:
    ins[1] = int(ins[1])
# print(instructions)


def iter_instructions(instructions, i=0, accumulator=0, seen=list()):
    if i in seen:
        return accumulator, seen, 1
    seen.append(i)
    try:
        ins = instructions[i]
    except IndexError:
        print("\nindex out of range", i, "for length", len(instructions), ", normal ending.")
        return accumulator, seen, 0
    if ins[0] == "jmp":
        return iter_instructions(instructions, i + ins[1], accumulator, seen)
    if ins[0] == "acc":
        accumulator += ins[1]
    return iter_instructions(instructions, i + 1, accumulator, seen)


accumulator, seen, exit_code = iter_instructions(instructions)
print(f"Just before the begining of infinite loop, {accumulator=}")

potential_anomaly = {i: instructions[i] for i in seen if instructions[i][0] != "acc"}
potential_anomaly_indexes = list(seen)
iter_anomaly = len(potential_anomaly_indexes) - 1
while exit_code != 0:
    tested = list(instructions)
    anomaly_index = potential_anomaly_indexes[iter_anomaly]
    tested[anomaly_index][0] = "nop" if instructions[anomaly_index][0] == "jmp" else "jmp"
    accumulator, seen, exit_code = iter_instructions(tested, seen=list())
    iter_anomaly += -1

# print(f"{seen=}")
print(f"{anomaly_index=}, {accumulator=}")
