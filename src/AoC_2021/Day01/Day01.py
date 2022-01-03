from aocd.transforms import numbers

from src.aoc_frame import run_part


def part_a(input_data: str) -> str:

    depths = numbers(input_data)
    increases = 0
    for i in range(len(depths) - 1):
        if depths[i] < depths[i+1]:
            increases += 1

    return increases


def part_b(input_data: str) -> str:
    depths = numbers(input_data)
    increases = 0

    depth_sums = [depths[i] + depths[i+1] + depths[i+2] for i in range(len(depths)-2)]

    for i in range(len(depth_sums) - 1):
        if depth_sums[i] < depth_sums[i+1]:
            increases += 1

    return increases


def better_part_b(input_data: str) -> str:
    depths = numbers(input_data)
    increases = 0
    for i in range(len(depths) - 3):
        if depths[i] < depths[i+3]:
            increases += 1

    return increases


run_part(part_a, 'a', 2021, 1)
# run_part(part_b, 'b', 2021, 1)
run_part(better_part_b, 'b', 2021, 1)

