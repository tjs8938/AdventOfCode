import functools
import itertools

from aocd.transforms import lines

from src.aoc_frame import run_part


def part_a(input_data: str) -> str:
    input_lines = lines(input_data)

    found = {}

    for line in input_lines:
        key = str(2020 - int(line))
        if line in found:
            print("Found " + key + " and " + line + " which multiply to " + str(int(key) * int(line)))
            return str(int(key) * int(line))
        else:
            found[key] = line


def part_b(input_data: str) -> str:
    input_lines = lines(input_data)

    for tup in itertools.product(input_lines, input_lines, input_lines):
        if functools.reduce(lambda a, b: int(a) + int(b), tup) == 2020:
            print("Found " + str(tup))
            return str(int(tup[0]) * int(tup[1]) * int(tup[2]))


run_part(part_a, 'a', 2020, 1)
run_part(part_b, 'b', 2020, 1)
