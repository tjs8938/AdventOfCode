from typing import Set, Tuple, Dict, List

from src.AoC_2017.Day10.HashKnot import HashKnot


class Region:

    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.neighbors: Set[Region] = set()
        self.group = -1

    @staticmethod
    def link_neighbors(a, b):
        a.neighbors.add(b)
        b.neighbors.add(a)

    def set_group(self, g: int):
        if self.group < 0:
            self.group = g
        for n in self.neighbors:
            if n.group < 0:
                n.set_group(g)


key = "jxqlasbh-"

mem_blocks: Dict[Tuple[int, int], Region] = {}
for y in range(128):
    k = key + str(y)
    knot = HashKnot(k).hash()
    binary = bin(int(knot, 16))[2:].zfill(128)
    for x in range(len(binary)):
        if binary[x] == '1':
            mem_blocks[(x, y)] = Region(x, y)
            if (x-1, y) in mem_blocks:
                Region.link_neighbors(mem_blocks[(x - 1, y)], mem_blocks[(x, y)])

            if (x, y - 1) in mem_blocks:
                Region.link_neighbors(mem_blocks[(x, y - 1)], mem_blocks[(x, y)])

region_count = 0
for r in mem_blocks.values():
    if r.group < 0:
        r.set_group(region_count)
        region_count += 1

print(region_count)
