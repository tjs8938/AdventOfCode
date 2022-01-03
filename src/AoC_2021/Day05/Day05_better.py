import itertools
import re
from collections import defaultdict
from typing import List, Tuple, Set

from aocd.transforms import lines

from src.aoc_frame import run_part


def parse_input(input_data: str) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    l = lines(input_data)
    pattern = re.compile("([0-9]*),([0-9]*) -> ([0-9]*),([0-9]*)")
    output = []
    for line in l:
        m = pattern.match(line)
        output.append(((int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))))

    return output


def points_on_line(line: Tuple[Tuple[int, int], Tuple[int, int]]) -> Set[Tuple[int, int]]:
    points = set()
    if line[0][0] != line[1][0] and line[0][1] == line[1][1]:
        # Horizontal line
        x1 = min(line[0][0], line[1][0])
        x2 = max(line[0][0], line[1][0])
        for x in range(x1, x2+1):
            points.add((x, line[0][1]))

    elif line[0][1] != line[1][1] and line[0][0] == line[1][0]:
        # Vertical line
        y1 = min(line[0][1], line[1][1])
        y2 = max(line[0][1], line[1][1])
        for y in range(y1, y2+1):
            points.add((line[0][0], y))

    else:
        x_inc = 1 if line[0][0] < line[1][0] else -1
        y_inc = 1 if line[0][1] < line[1][1] else -1

        for x, y in zip(range(line[0][0], line[1][0] + x_inc, x_inc), range(line[0][1], line[1][1] + y_inc, y_inc)):
            points.add((x, y))

    return points


def part_a(input_data: str) -> str:
    points = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], parse_input(input_data)))

    intersect_points = find_intersections(points)

    return str(intersect_points)


def part_b(input_data: str) -> str:
    points = parse_input(input_data)

    intersect_points = find_intersections(points)

    return str(intersect_points)


def find_intersections(in_lines):
    points = defaultdict(int)
    for line in in_lines:
        for p in points_on_line(line):
            points[p] += 1

    count = 0
    for n in points.values():
        if n > 1:
            count += 1
    return count


run_part(part_a, 'a', 2021, 5)
run_part(part_b, 'b', 2021, 5)

