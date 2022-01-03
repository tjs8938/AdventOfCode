from copy import copy
from typing import List, Callable

from aocd.transforms import lines

from src.aoc_frame import run_part


def part_a(input_data: str) -> str:
    nums = lines(input_data)
    bit_counts = []
    for num in nums:
        for i in range(len(num)):
            if len(bit_counts) <= i:
                bit_counts.append(0)
            if num[i] == '1':
                bit_counts[i] += 1

    gamma = 0
    for bit in bit_counts:
        gamma *= 2
        if bit > (len(nums) / 2):
            gamma += 1
    epsilon = pow(2, len(bit_counts)) - 1 - gamma
    return gamma * epsilon


def find_rating(readings: List[str], pred: Callable[[List[str], List[str]], bool]) -> int:
    remaining = copy(readings)
    bit_pos = 0

    while len(remaining) > 1:
        one_bits = []
        zero_bits = []

        for r in remaining:
            (one_bits if r[bit_pos] == '1' else zero_bits).append(r)
        remaining = one_bits if pred(one_bits, zero_bits) else zero_bits
        bit_pos += 1

    return int(remaining[0], 2)


def part_b(input_data: str) -> str:
    nums = lines(input_data)

    o2_rating = find_rating(nums, lambda x, y: len(x) >= len(y))
    co2_rating = find_rating(nums, lambda x, y: len(x) < len(y))

    return o2_rating * co2_rating


run_part(part_a, 'a', 2021, 3)
run_part(part_b, 'b', 2021, 3)

