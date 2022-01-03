import itertools
from collections import deque

import numpy as np
from aocd.transforms import lines

from src.aoc_frame import run_part


def part_a(input_data: str) -> str:
    octos = np.array([[int(x) for x in line] for line in lines(input_data)])
    total_flashes = 0

    for i in range(100):
        flashers = deque()
        seen = set()

        octos += 1

        for y in range(10):
            for x in range(10):
                if octos[y][x] > 9:
                    flashers.append((x, y))
                    seen.add((x, y))

        while len(flashers) > 0:
            flasher = flashers.popleft()
            for direction in itertools.product([-1, 0, 1], repeat=2):
                loc = (flasher[0] + direction[0], flasher[1] + direction[1])
                if loc[0] in range(10) and loc[1] in range(10) and loc not in seen:
                    octos[loc[1]][loc[0]] += 1
                    if octos[loc[1]][loc[0]] > 9:
                        flashers.append(loc)
                        seen.add(loc)

        total_flashes += np.count_nonzero(octos > 9)
        octos[octos > 9] = 0

    print(total_flashes)
    return str(total_flashes)


def part_b(input_data: str) -> str:
    octos = np.array([[int(x) for x in line] for line in lines(input_data)])

    i = 1
    while True:
        flashers = deque()
        seen = set()

        octos += 1

        for y in range(10):
            for x in range(10):
                if octos[y][x] > 9:
                    flashers.append((x, y))
                    seen.add((x, y))

        while len(flashers) > 0:
            flasher = flashers.popleft()
            for direction in itertools.product([-1, 0, 1], repeat=2):
                loc = (flasher[0] + direction[0], flasher[1] + direction[1])
                if loc[0] in range(10) and loc[1] in range(10) and loc not in seen:
                    octos[loc[1]][loc[0]] += 1
                    if octos[loc[1]][loc[0]] > 9:
                        flashers.append(loc)
                        seen.add(loc)

        if np.count_nonzero(octos > 9) == 100:
            return str(i)
        octos[octos > 9] = 0
        i += 1


# run_part(part_a, 'a', 2021, 11)
run_part(part_b, 'b', 2021, 11)

