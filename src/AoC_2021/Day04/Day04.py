from pprint import pprint
from typing import Tuple, List

from src.aoc_frame import run_part
from aocd.transforms import lines


def parse_input(input_data: str) -> Tuple[List[int], List[List[int]]]:
    l = lines(input_data)
    draws = [int(x) for x in l[0].split(',')]

    boards: List[List[int]] = []
    line_index = 2
    while line_index < len(l):
        b: List[int] = []
        for r in range(line_index, line_index + 5):
            row = [int(x) for x in l[r].split()]
            b.extend(row)
        line_index += 6
        boards.append(b)
    return draws, boards


def board_wins(board) -> bool:
    winning_masks = ["11111", "1111100000", "111110000000000", "11111000000000000000", "1111100000000000000000000",
                     "100001000010000100001", "1000010000100001000010", "10000100001000010000100",
                     "100001000010000100001000", "1000010000100001000010000"]
    for w in winning_masks:
        if (int(w, 2) & board) == int(w, 2):
            return True
    return False


def sum_remaining(board) -> int:
    return sum(filter(lambda x: x != -1, board))


def part_a(input_data: str) -> str:
    draws, boards = parse_input(input_data)

    d = 0
    spots_marked = [0 for i in range(len(boards))]

    while True:
        draw = draws[d]

        for b_index in range(len(boards)):
            board = boards[b_index]
            if draw in board:
                i = board.index(draw)
                board[i] = -1
                spots_marked[b_index] |= 1 << i

                if board_wins(spots_marked[b_index]):
                    score = sum_remaining(board) * draw
                    return str(score)
        d += 1


def part_b(input_data: str) -> str:
    draws, boards = parse_input(input_data)

    d = 0
    spots_marked = [0 for i in range(len(boards))]

    while True:
        draw = draws[d]
        winning_board_list = []

        for b_index in range(len(boards)):
            board = boards[b_index]
            if draw in board:
                i = board.index(draw)
                board[i] = -1
                spots_marked[b_index] |= 1 << i

                if board_wins(spots_marked[b_index]):
                    winning_board_list.append(b_index)

                if len(winning_board_list) == len(boards):
                    score = sum_remaining(board) * draw
                    return str(score)

        for winning_board in winning_board_list[::-1]:
            boards.pop(winning_board)
            spots_marked.pop(winning_board)
        d += 1


# run_part(part_a, 'a', 2021, 4)
run_part(part_b, 'b', 2021, 4)

