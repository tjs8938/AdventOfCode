import itertools
import re
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

    return str(len(intersect_points))


def part_b(input_data: str) -> str:
    points = parse_input(input_data)

    intersect_points = find_intersections(points)

    return str(len(intersect_points))


def find_intersections(points):
    intersect_points = set()
    for l1, l2 in itertools.combinations(points, 2):

        inner_x_max = max(min(l1[0][0], l1[1][0]), min(l2[0][0], l2[1][0]))
        inner_x_min = min(max(l1[0][0], l1[1][0]), max(l2[0][0], l2[1][0]))
        inner_y_max = max(min(l1[0][1], l1[1][1]), min(l2[0][1], l2[1][1]))
        inner_y_min = min(max(l1[0][1], l1[1][1]), max(l2[0][1], l2[1][1]))
        if inner_y_min >= inner_y_max or inner_x_min >= inner_x_max:

            l1_points = points_on_line(l1)
            l2_points = points_on_line(l2)

            cross = l1_points.intersection(l2_points)
            intersect_points = intersect_points.union(cross)
    return intersect_points


# run_part(part_a, 'a', 2021, 5)
run_part(part_b, 'b', 2021, 5)

