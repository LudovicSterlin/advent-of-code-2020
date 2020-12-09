import os

os.chdir(os.path.dirname(__file__))


def get_lines(file_path, verbose=True):
    with open(file_path) as f:
        lines = f.readlines()
    print(f"Found {len(lines)} lines in {file_path.split('/')[-1]}")
    return lines


lines = get_lines("./input.txt")
numbers = [int(line) for line in lines]
SUM_TARGET = 2020
for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == SUM_TARGET:
            print(f"\n2 Entries that sum up to {SUM_TARGET} are {numbers[i]} and {numbers[j]}")
            print(f"\t {numbers[i]}*{numbers[j]}={numbers[i]*numbers[j]}")
            break

for i in range(len(numbers) - 2):
    for j in range(i + 1, len(numbers) - 1):
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == SUM_TARGET:
                print(f"\n3 Entries that sum up to {SUM_TARGET} are {numbers[i]} + {numbers[j]} + {numbers[k]}")
                print(f"\t {numbers[i]}*{numbers[j]}*{numbers[k]}={numbers[i]*numbers[j]*numbers[k]}")
                break
