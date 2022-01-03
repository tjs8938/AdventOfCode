import itertools
from pprint import pprint

import numpy as np
from aocd.transforms import lines

from src.Utility.MatrixPrint import print_matrix
from src.aoc_frame import run_part


def part_a(input_data: str) -> str:
    cukes = np.array([[c for c in line] for line in lines(input_data)])

    for step in itertools.count(start=1):
        move_count = 0
        # Move sea cucumbers to the right if they are unblocked
        roll_right = np.roll(cukes, 1, 1)
        roll_left = np.roll(cukes, -1, 1)

        cur_mask = np.bitwise_and(cukes == '>', roll_left == '.')
        next_mask = np.bitwise_and(cukes == '.', roll_right == '>')
        move_count += np.count_nonzero(next_mask)
        cukes[cur_mask] = '.'
        cukes[next_mask] = '>'

        # Move sea cucumbers to the down if they are unblocked
        roll_down = np.roll(cukes, 1, 0)
        roll_up = np.roll(cukes, -1, 0)

        cur_mask = np.bitwise_and(cukes == 'v', roll_up == '.')
        next_mask = np.bitwise_and(cukes == '.', roll_down == 'v')
        move_count += np.count_nonzero(next_mask)

        cukes[cur_mask] = '.'
        cukes[next_mask] = 'v'

        # print("After {} steps:".format(step))
        # print_matrix(cukes)
        # print()
        if move_count == 0:
            break
    return str(step)


def part_b(input_data: str) -> str:
    return 'B'


run_part(part_a, 'a', 2021, 25)
# run_part(part_b, 'b', 2021, 25)

