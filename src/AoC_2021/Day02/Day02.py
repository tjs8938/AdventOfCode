import re

from aocd.transforms import lines

from src.aoc_frame import run_part


def part_a(input_data: str) -> str:
    moves = lines(input_data)
    pattern = re.compile("(forward|down|up) ([0-9]*)")

    position = [0, 0]

    for move in moves:
        m = pattern.match(move)
        direction = m.group(1)
        dist = int(m.group(2))
        if direction == 'forward':
            position[0] += dist
        elif direction == 'down':
            position[1] += dist
        else:
            position[1] -= dist

    return position[0] * position[1]


def part_b(input_data: str) -> str:
    moves = lines(input_data)
    pattern = re.compile("(forward|down|up) ([0-9]*)")

    position = [0, 0]
    aim = 0

    for move in moves:
        m = pattern.match(move)
        direction = m.group(1)
        dist = int(m.group(2))
        if direction == 'forward':
            position[0] += dist
            position[1] += dist * aim
        elif direction == 'down':
            aim += dist
        else:
            aim -= dist

    return position[0] * position[1]


#run_part(part_a, 'a', 2021, 2)
run_part(part_b, 'b', 2021, 2)

