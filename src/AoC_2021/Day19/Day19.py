import itertools
import operator
import re
from collections import defaultdict
from pprint import pprint
from typing import List, Tuple, Dict, Optional, Set

from aocd.transforms import lines

from src.aoc_frame import run_part

rotations = [
    # rotate around z
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (-y, x, z),
    lambda x, y, z: (-x, -y, z),
    lambda x, y, z: (y, -x, z),

    # rotate x 90, then rotate around z
    lambda x, y, z: (x, -z, y),
    lambda x, y, z: (z, x, y),
    lambda x, y, z: (-x, z, y),
    lambda x, y, z: (-z, -x, y),

    # rotate x 180, then rotate around z
    lambda x, y, z: (x, -y, -z),
    lambda x, y, z: (y, x, -z),
    lambda x, y, z: (-x, y, -z),
    lambda x, y, z: (-y, -x, -z),

    # rotate x 270, then rotate around z
    lambda x, y, z: (x, z, -y),
    lambda x, y, z: (-z, x, -y),
    lambda x, y, z: (-x, -z, -y),
    lambda x, y, z: (z, -x, -y),

    # rotate y 90, then rotate around z
    lambda x, y, z: (z, y, -x),
    lambda x, y, z: (-y, z, -x),
    lambda x, y, z: (-z, -y, -x),
    lambda x, y, z: (y, -z, -x),

    # rotate y 270, then rotate around z
    lambda x, y, z: (-z, y, x),
    lambda x, y, z: (-y, -z, x),
    lambda x, y, z: (z, -y, x),
    lambda x, y, z: (y, z, x)
]


def parse_input(input_data: str) -> List[List[Tuple[int, int, int]]]:
    in_lines = lines(input_data)

    scanners = []
    beacons = []

    for line in in_lines[1:]:
        if line == '':
            continue
        elif str.find(line, "scanner") > 0:
            scanners.append(beacons)
            beacons = []
        else:
            splits = [int(x) for x in line.split(',')]
            beacons.append((splits[0], splits[1], splits[2]))

    scanners.append(beacons)
    return scanners


def find_position_from_overlap(a: List[Tuple[int, int, int]], b: List[Tuple[int, int, int]]) -> Optional[Tuple[int, int, int]]:
    resulting_location: Dict[Tuple[int, int, int], int] = defaultdict(int)

    for a_m, b_n in itertools.product(a, b):
        loc = (a_m[0] - b_n[0], a_m[1] - b_n[1], a_m[2] - b_n[2])
        resulting_location[loc] += 1
        if resulting_location[loc] >= 12:
            return loc

    return None


def scanner_and_beacon_positions(input_data):
    scanners = parse_input(input_data)
    scanner_positions: List[Optional[Tuple[int, int, int]]] = [None for s in scanners]
    scanner_positions[0] = (0, 0, 0)
    found_scanners = [0]
    all_beacons: Set[Tuple[int, int, int]] = set()
    all_beacons.update(scanners[0])
    while len(found_scanners) > 0:
        known_index = found_scanners.pop()
        known_scanner = scanners[known_index]
        known_scanner_position = scanner_positions[known_index]

        for unknown_index in filter(lambda j: scanner_positions[j] is None, range(len(scanners))):
            unknown = scanners[unknown_index]
            for orientation in rotations:
                rotated_unknown = list(map(lambda x: orientation(*x), unknown))
                position = find_position_from_overlap(known_scanner, rotated_unknown)
                if position is not None:
                    position = (known_scanner_position[0] + position[0], known_scanner_position[1] + position[1],
                                known_scanner_position[2] + position[2])
                    scanners[unknown_index] = rotated_unknown
                    scanner_positions[unknown_index] = position
                    found_scanners.append(unknown_index)

                    for loc in rotated_unknown:
                        all_beacons.add((loc[0] + position[0], loc[1] + position[1], loc[2] + position[2]))

                    break
    return scanner_positions, all_beacons


def part_a(input_data: str) -> str:
    all_scanners, all_beacons = scanner_and_beacon_positions(input_data)
    return str(len(all_beacons))


def part_b(input_data: str) -> str:
    all_scanners, all_beacons = scanner_and_beacon_positions(input_data)
    furthest = 0
    for a, b in itertools.combinations(all_scanners, 2):
        dist = abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])
        if dist > furthest:
            furthest = dist

    return str(furthest)


# run_part(part_a, 'a', 2021, 19)
run_part(part_b, 'b', 2021, 19)
