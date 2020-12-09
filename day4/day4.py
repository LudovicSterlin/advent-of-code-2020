import os
import re

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


def check_item(key, value):
    if k == "byr":
        value = int(value)
        return 1920 <= value and value <= 2002
    if k == "iyr":
        value = int(value)
        return 2010 <= value and value <= 2020
    if k == "eyr":
        value = int(value)
        return 2020 <= value and value <= 2030
    if k == "hgt":
        unit = value[-2:]
        if unit in ["cm", "in"]:
            height = int(value[:-2])
            if unit == "cm":
                return 150 <= height and height <= 193
            if unit == "in":
                return 59 <= height and height <= 76
        return False
    if k == "hcl":
        hcl = re.compile("#[a-f0-9]{6}")
        return hcl.match(value)
    if k == "ecl":
        valid_values = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return value in valid_values
    if k == "pid":
        return value.isdecimal() and len(value) == 9
    if k == "cid":
        raise KeyError("'cid' should have been removed")
        return True
    raise KeyError(key, "should not be present")
    return False


passeports = get_block_between_blanklines("./input.txt")
passeports = [p.replace("\n", " ") for p in passeports]
passeports = [p.split() for p in passeports]

labels = [
    "byr (Birth Year)",
    "iyr (Issue Year)",
    "eyr (Expiration Year)",
    "hgt (Height)",
    "hcl (Hair Color)",
    "ecl (Eye Color)",
    "pid (Passport ID)",
    "cid (Country ID)",
]
print(f"{labels=}")
req_fields = set([label.split()[0] for label in labels])
req_fields.remove("cid")
print(f"{req_fields=}")

req_fields_present = 0
passeports_to_check = []
for passeport in passeports:
    fields = set([f.split(":")[0] for f in passeport])
    if req_fields.issubset(fields):
        req_fields_present += 1
        pass_dict = dict([f.split(":") for f in passeport])
        pass_dict.pop("cid", None)
        passeports_to_check.append(pass_dict)

all_fields_valid = 0
for passeport in passeports_to_check:
    valid = True
    for k, v in passeport.items():
        if not check_item(k, v):
            valid = False
            break
    if valid:
        all_fields_valid += 1


print(f"There is {req_fields_present} passeports with required fields present")
print(f"\nThere is {all_fields_valid} passeports with all_fields_valid")
