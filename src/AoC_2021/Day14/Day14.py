from collections import defaultdict

from aocd.transforms import lines

from src.aoc_frame import run_part


def part_a(input_data: str) -> str:
    in_lines = lines(input_data)
    polymer = in_lines[0]
    rules = {}

    for rule_line in in_lines[2:]:
        rules[rule_line[:2]] = rule_line[-1]

    for stage in range(10):
        new_polymer = polymer[0]

        for index in range(len(polymer) - 1):
            pair = polymer[index:index+2]
            new_polymer += rules[pair] + polymer[index + 1]

        print("After step " + str(stage + 1) + ": " + new_polymer)
        polymer = new_polymer

    e_counts = {}
    for element in polymer:
        if element not in e_counts:
            e_counts[element] = str.count(polymer, element)

    pair_list = list(e_counts.items())
    pair_list.sort(key=lambda x: x[1])
    print(pair_list)

    return str(pair_list[-1][1] - pair_list[0][1])


def part_a_better(input_data: str) -> str:
    return solve(input_data)


def solve(input_data: str, steps=10) -> str:
    in_lines = lines(input_data)
    rules = {}

    for rule_line in in_lines[2:]:
        rules[rule_line[:2]] = (rule_line[0] + rule_line[-1], rule_line[-1] + rule_line[1])

    polymer = defaultdict(int)
    for i in range(len(in_lines[0]) - 1):
        polymer[in_lines[0][i:i+2]] = 1

    for stage in range(steps):
        new_polymer = defaultdict(int)
        for pair, count in polymer.items():
            rule = rules[pair]
            new_polymer[rule[0]] += count
            new_polymer[rule[1]] += count

        polymer = new_polymer

    # All but first and last char are double counted
    e_counts = defaultdict(int)
    for pair, count in polymer.items():
        e_counts[pair[0]] += count
        e_counts[pair[1]] += count

    # add 1 for first and last
    e_counts[in_lines[0][0]] += 1
    e_counts[in_lines[0][-1]] += 1

    pair_list = list(e_counts.items())
    pair_list.sort(key=lambda x: x[1])
    print(pair_list)

    # Halve to account for double counting
    most = pair_list[-1][1] / 2
    least = pair_list[0][1] / 2
    return str(int(most - least))


def part_b(input_data: str) -> str:
    return solve(input_data, steps=40)


# run_part(part_a_better, 'a', 2021, 14)
run_part(part_b, 'b', 2021, 14)

