
import numpy as np

from src.aoc_frame import run_part


def part_a(input_data: str) -> str:
    positions = np.array([int(x) for x in input_data.split(',')])
    median = np.median(positions)

    cost = sum([abs(median - p) for p in positions])
    return str(int(cost))


def part_b(input_data: str) -> str:
    positions = np.array([int(x) for x in input_data.split(',')])

    costs = []
    for d in range(positions.min(), positions.max() + 1):
        costs.append(sum([(abs(d - p) * (abs(d - p) + 1)) // 2 for p in positions]))
    cost = min(costs)
    return str(int(cost))


def part_b_numpy(input_data: str) -> str:
    positions = np.array([int(x) for x in input_data.split(',')]).reshape(1, -1)

    targets = np.arange(positions.min(), positions.max() + 1).reshape(-1, 1)
    costs = (abs(targets - positions) * (abs(targets - positions) + 1)) // 2

    return str(int(costs.sum(axis=1).min()))


def part_b_mean(input_data: str) -> str:
    positions = np.array([int(x) for x in input_data.split(',')])
    mean = int(round(np.mean(positions)))

    costs = []
    for d in range(mean - 1, mean + 2):
        costs.append(sum([(abs(d - p) * (abs(d - p) + 1)) // 2 for p in positions]))
    cost = min(costs)
    return str(int(cost))


def part_b_numpy_mean(input_data: str) -> str:
    positions = np.array([int(x) for x in input_data.split(',')]).reshape(1, -1)
    mean = int(round(np.mean(positions)))

    targets = np.arange(mean - 1, mean + 2).reshape(-1, 1)
    costs = (abs(targets - positions) * (abs(targets - positions) + 1)) // 2

    return str(int(costs.sum(axis=1).min()))


# run_part(part_a, 'a', 2021, 7)
run_part(part_b, 'b', 2021, 7)
run_part(part_b_numpy, 'b', 2021, 7)
run_part(part_b_mean, 'b', 2021, 7)
run_part(part_b_numpy_mean, 'b', 2021, 7)
