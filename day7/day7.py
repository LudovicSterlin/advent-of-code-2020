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


def create_bag(rule):
    bag = " ".join(rule.split(" ")[:2])
    contain_bags = rule.split("contain")[1].split(",")
    nb_bags = [int(cb.split(" ")[1]) for cb in contain_bags if "no other" not in cb]
    contain_bags = [" ".join(cb.split(" ")[-3:-1]) for cb in contain_bags if "no other" not in cb]
    return bag, contain_bags, nb_bags


lines = [line[:-2] for line in get_lines("./input.txt")]
bags = defaultdict(set)
bags_count = defaultdict(set)
for line in lines:
    bag, contain_bags, nb_bags = create_bag(line)
    bags[bag] = contain_bags
    bags_count[bag] = nb_bags


def search_container(target_bag, bags):
    if len(bags) == 0:
        return [target_bag]
    containers = [target_bag]
    for bag in [b for b, v in bags.items() if target_bag in v]:
        containers += search_container(bag, bags)
    return containers


TARGET = "shiny gold"
shiny_gold_containers = set(search_container(TARGET, bags))
print(f"Found {len(shiny_gold_containers)-1} containers for '{TARGET}'")


def count_bag_inside(target_bag, bags, bags_count):
    if len(bags[target_bag]) == 0:
        return 0
    inside = sum(bags_count[target_bag])
    for i, bag in enumerate(bags[target_bag]):
        inside += bags_count[target_bag][i] * count_bag_inside(bag, bags, bags_count)
    return inside


print(f"'{TARGET}' need {count_bag_inside(TARGET, bags, bags_count)} bags inside")
