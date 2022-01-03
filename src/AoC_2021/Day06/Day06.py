from collections import deque

import numpy as np

from src.aoc_frame import run_part


def part_a(input_data: str) -> str:
    fish = np.array([int(x) for x in input_data.split(',')])

    for day in range(80):
        ready_fish = np.count_nonzero(fish == 0)
        fish = np.append(fish, np.repeat(9, ready_fish))
        fish[fish == 0] = 7
        print(fish)
        fish = fish - 1

    return str(len(fish))


def part_b(input_data: str) -> str:
    fish = deque([0 for i in range(9)])
    in_fish = [int(x) for x in input_data.split(',')]
    for f in in_fish:
        fish[f] += 1

    for day in range(256):
        ready_fish = fish.popleft()
        fish[6] += ready_fish
        fish.append(ready_fish)

    total_fish = sum(fish)
    return str(total_fish)


# run_part(part_a, 'a', 2021, 6)
run_part(part_b, 'b', 2021, 6)

