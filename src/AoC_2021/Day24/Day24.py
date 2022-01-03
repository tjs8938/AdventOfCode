import itertools
from collections import defaultdict
from functools import lru_cache
from typing import List, Dict

from aocd.transforms import lines

from src.aoc_frame import run_part


@lru_cache
def calc_next(z, next_w: str, div_val: int, x_add: int, y_add: int):
    w = int(next_w)
    x = (z % 26) + x_add
    z = int(z // div_val)
    x = 1 if x != w else 0
    y = 25 * x + 1
    z = z * y
    y = (w + y_add) * x
    z += y
    return z

#
# inputs = [
#     [1, 14,  1],
#     [1, 15,  7],
#     [1, 15,  13],
#     [26, -6, 10],
#     [1, 14,  0],
#     [26, -4, 13],
#     [1, 15,  11],
#     [1, 15,  6],
#     [1, 11,  1],
#     [26, 0,  7],
#     [26, 0,  11],
#     [26, -3, 14],
#     [26, -9, 4],
#     [26, -9, 10]
# ]


def parse_inputs(input_data):
    in_lines = lines(input_data)
    inputs = []
    for instruction in range(14):
        div_inst = int(in_lines[instruction * 18 + 4].split()[-1])
        x_add_inst = int(in_lines[instruction * 18 + 5].split()[-1])
        y_add_inst = int(in_lines[instruction * 18 + 15].split()[-1])
        inputs.append([div_inst, x_add_inst, y_add_inst])

    return inputs


def part_a(input_data: str) -> str:
    inputs = parse_inputs(input_data)
    options = build_options(inputs)

    return ''.join(map(lambda x: x[1][0], sorted(list(options.items()), key=lambda x: x[0])))


def part_b(input_data: str) -> str:
    inputs = parse_inputs(input_data)
    options = build_options(inputs)

    return ''.join(map(lambda x: x[1][-1], sorted(list(options.items()), key=lambda x: x[0])))


def build_options(inputs):
    stack = []
    pairs = []
    for idx, g in enumerate(inputs):
        if g[0] == 1:
            stack.append((g, idx))
        else:
            pairs.append((stack.pop(), (g, idx)))
    options: Dict[int, List[int]] = defaultdict(list)
    values = ['9', '8', '7', '6', '5', '4', '3', '2', '1']
    for pair in pairs:
        for up, down in itertools.product(values, repeat=2):
            middle = calc_next(0, up, *pair[0][0])
            result = calc_next(middle, down, *pair[1][0])
            if result == 0:
                options[pair[0][1]].append(up)
                options[pair[1][1]].append(down)
    return options


run_part(part_a, 'a', 2021, 24)
run_part(part_b, 'b', 2021, 24)

