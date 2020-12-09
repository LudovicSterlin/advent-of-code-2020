import os
from collections import defaultdict

os.chdir(os.path.dirname(__file__))


def get_lines(file_path, verbose=True):
    with open(file_path) as f:
        lines = f.readlines()
    print(f"Found {len(lines)} lines in {file_path.split('/')[-1]}")
    return lines


def check_password_part1(policy, letter, password):
    min, max = [int(x) for x in policy.split("-")]
    nb = password.count(letter)
    return min <= nb and nb <= max


def check_password_part2(policy, letter, password):
    i1, i2 = [int(x) for x in policy.split("-")]
    return (password[i1 - 1] == letter) != (password[i2 - 1] == letter)


lines = get_lines("./input.txt")
counts1 = defaultdict(int)
counts2 = defaultdict(int)
# lines = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
for line in lines:
    policy, letter, password = line.split()
    letter = letter[0]
    counts1[str(check_password_part1(policy, letter, password))] += 1
    counts2[str(check_password_part2(policy, letter, password))] += 1

print("\1Part1")
for k, v in counts1.items():
    print(f"{k}: {v}")

print("\1Part2")
for k, v in counts2.items():
    print(f"{k}: {v}")
