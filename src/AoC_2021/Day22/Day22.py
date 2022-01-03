from __future__ import annotations

import dataclasses
import re
from dataclasses import dataclass
from typing import List

from aocd.transforms import lines

from src.aoc_frame import run_part


@dataclass
class Region:
    x0: int
    x1: int
    y0: int
    y1: int
    z0: int
    z1: int

    def has_overlap(self, other: Region) -> bool:
        return self.x0 <= other.x1 and self.x1 >= other.x0 and \
            self.y0 <= other.y1 and self.y1 >= other.y0 and \
            self.z0 <= other.z1 and self.z1 >= other.z0

    def size(self):
        return (self.x1 - self.x0 + 1) * (self.y1 - self.y0 + 1) * (self.z1 - self.z0 + 1)


def part_a(input_data: str) -> str:
    def pred(ranges: List[int]):
        return all([-50 <= n <= 50 for n in ranges])
    return process_instructions(input_data, instr_filter=pred)


def part_b(input_data: str) -> str:
    return process_instructions(input_data)


def process_instructions(input_data, instr_filter=None):
    in_lines = lines(input_data)
    pattern = re.compile("(on|off) x=(-?[0-9]*)\.\.(-?[0-9]*),y=(-?[0-9]*)\.\.(-?[0-9]*),z=(-?[0-9]*)\.\.(-?[0-9]*)")
    regions: List[Region] = []
    for step in in_lines:
        m = pattern.match(step)
        command = m.group(1)
        ranges = list(map(lambda n: int(n), m.group(2, 3, 4, 5, 6, 7)))
        if instr_filter is not None and not instr_filter(ranges):
            continue

        region = Region(*ranges)

        new_regions: List[Region] = []
        for old_region in regions:
            if old_region.has_overlap(region):
                # here is where the subtraction happens
                if old_region.x0 < region.x0:
                    # new region with everything "left" of the old region
                    copy = dataclasses.replace(old_region)
                    copy.x1 = region.x0 - 1
                    new_regions.append(copy)
                if old_region.x1 > region.x1:
                    # new region with everything "right" of the old region
                    copy = dataclasses.replace(old_region)
                    copy.x0 = region.x1 + 1
                    new_regions.append(copy)
                if old_region.y0 < region.y0:
                    # new region with everything "below" of the old region
                    copy = dataclasses.replace(old_region)
                    copy.y1 = region.y0 - 1
                    if old_region.x0 < region.x0:
                        copy.x0 = region.x0
                    if old_region.x1 > region.x1:
                        copy.x1 = region.x1
                    new_regions.append(copy)
                if old_region.y1 > region.y1:
                    # new region with everything "above" of the old region
                    copy = dataclasses.replace(old_region)
                    copy.y0 = region.y1 + 1
                    if old_region.x0 < region.x0:
                        copy.x0 = region.x0
                    if old_region.x1 > region.x1:
                        copy.x1 = region.x1
                    new_regions.append(copy)

                if old_region.z0 < region.z0:
                    # new region with everything "in front" of the old region
                    copy = dataclasses.replace(old_region)
                    copy.z1 = region.z0 - 1
                    if old_region.x0 < region.x0:
                        copy.x0 = region.x0
                    if old_region.x1 > region.x1:
                        copy.x1 = region.x1
                    if old_region.y0 < region.y0:
                        copy.y0 = region.y0
                    if old_region.y1 > region.y1:
                        copy.y1 = region.y1
                    new_regions.append(copy)
                if old_region.z1 > region.z1:
                    # new region with everything "in back" of the old region
                    copy = dataclasses.replace(old_region)
                    copy.z0 = region.z1 + 1
                    if old_region.x0 < region.x0:
                        copy.x0 = region.x0
                    if old_region.x1 > region.x1:
                        copy.x1 = region.x1
                    if old_region.y0 < region.y0:
                        copy.y0 = region.y0
                    if old_region.y1 > region.y1:
                        copy.y1 = region.y1
                    new_regions.append(copy)
            else:
                new_regions.append(old_region)

        regions = new_regions
        if command == 'on':
            regions.append(region)
    return sum(map(lambda n: n.size(), regions))


run_part(part_a, 'a', 2021, 22)
run_part(part_b, 'b', 2021, 22)

