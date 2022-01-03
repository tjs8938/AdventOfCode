from pprint import pprint
from typing import Tuple, List

import numpy as np
from numpy import ndarray

from src.aoc_frame import run_part
from aocd.transforms import lines


def parse_input(input_data: str) -> Tuple[List[int], ndarray]:
    first_newline = input_data.index('\n')
    draws = [int(x) for x in input_data[:first_newline].split(',')]

    boards = np.array([int(x) for x in input_data[first_newline:].split()]).reshape(-1, 5, 5)
    return draws, boards


def part_a(input_data: str) -> str:
    draws, boards = parse_input(input_data)
    d = 0

    while True:
        draw = draws[d]

        boards[boards == draw] = -1

        for b_index in range(len(boards)):
            for i in range(5):
                if boards[b_index, :, i].sum() == -5 \
                        or boards[b_index, i, :].sum() == -5:
                    board = boards[b_index]
                    score = board[board != -1].sum() * draw
                    return str(score)
        d += 1


def part_b(input_data: str) -> str:
    draws, boards = parse_input(input_data)
    d = 0

    while True:
        draw = draws[d]

        boards[boards == draw] = -1

        for b_index in range(len(boards))[::-1]:
            for i in range(5):
                if boards[b_index, :, i].sum() == -5 \
                        or boards[b_index, i, :].sum() == -5:
                    if len(boards) == 1:
                        board = boards[b_index]
                        score = board[board != -1].sum() * draw
                        return str(score)
                    else:
                        boards = np.delete(boards, b_index, axis=0)
                        break
        d += 1


run_part(part_a, 'a', 2021, 4)
run_part(part_b, 'b', 2021, 4)
