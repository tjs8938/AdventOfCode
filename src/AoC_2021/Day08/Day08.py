from collections import defaultdict
from copy import copy

from aocd.transforms import lines

from src.aoc_frame import run_part


def part_a(input_data: str) -> str:
    count = 0
    for line in lines(input_data):
        outputs = line.split('|')[1].split()
        for o in outputs:
            if len(o) in [7, 4, 2, 3]:
                count += 1
    return str(count)


def part_b(input_data: str) -> str:
    running_sum = 0
    for line in lines(input_data):
        known_digits = {}
        patterns = line.split("|")[0].split()
        outputs = line.split("|")[1].split()

        p_lengths = defaultdict(list)
        for p in patterns:
            p_lengths[len(p)].append(p)

        one_pattern = p_lengths[2][0]
        known_digits[one_pattern] = 1

        four_pattern = p_lengths[4][0]
        known_digits[four_pattern] = 4

        eight_pattern = p_lengths[7][0]
        known_digits[eight_pattern] = 8

        seven_pattern = p_lengths[3][0]
        known_digits[seven_pattern] = 7

        one_segments = list(one_pattern)
        four_segments = list(filter(lambda x: x not in one_segments, list(four_pattern)))

        unknown_five_segments = p_lengths[5]
        for pattern in unknown_five_segments:
            if four_segments[0] in pattern and four_segments[1] in pattern:
                known_digits[pattern] = 5
            elif one_segments[0] in pattern and one_segments[1] in pattern:
                known_digits[pattern] = 3
            else:
                known_digits[pattern] = 2

        unknown_six_segments = p_lengths[6]
        for pattern in unknown_six_segments:
            if four_segments[0] in pattern and four_segments[1] in pattern and \
                    one_segments[0] in pattern and one_segments[1] in pattern:
                known_digits[pattern] = 9
            elif one_segments[0] in pattern and one_segments[1] in pattern:
                known_digits[pattern] = 0
            else:
                known_digits[pattern] = 6

        output_val = 0
        for output in outputs:
            output_val *= 10
            for key, value in known_digits.items():
                if set(key) == set(output):
                    output_val += value

                    break
        running_sum += output_val
    return str(running_sum)


# run_part(part_a, 'a', 2021, 8)
run_part(part_b, 'b', 2021, 8)

