from collections import deque
from typing import Dict, Tuple, Set

from aocd.transforms import lines

from src.Utility.NodeMap.Node import Node
from src.Utility.NodeMap.NodeMap import NodeMap
from src.aoc_frame import run_part


def part_a(input_data: str) -> str:
    heights = [[int(x) for x in line] for line in lines(input_data)]
    nodes = NodeMap(lines(input_data), Node)

    low_points = 0

    for loc in nodes.nodes.values():
        if all([heights[n.y][n.x] > heights[loc.y][loc.x] for n in loc.neighbors.values()]):
            low_points += 1 + heights[loc.y][loc.x]
    return str(low_points)


class Day09Node(Node):
    def __init__(self, x, y, symbol):
        super().__init__(x, y, symbol)

    def __lt__(self, other):
        return int(self.symbol) < int(other.symbol)

    def __gt__(self, other):
        return int(self.symbol) > int(other.symbol)


def part_b(input_data: str) -> str:
    heights = [[int(x) for x in line] for line in lines(input_data)]
    nodes = NodeMap(lines(input_data), Day09Node, blocked='9')
    basins: Dict[Tuple[int, int], Set[Tuple[int, int]]] = {}

    for loc in nodes.nodes.values():
        if all([heights[n.y][n.x] > heights[loc.y][loc.x] for n in loc.neighbors.values()]):
            basins[(loc.x, loc.y)] = {(loc.x, loc.y)}

    for basin_loc in basins:
        loc_queue = deque()
        loc_queue.append(nodes.get_node(basin_loc[0], basin_loc[1]))

        while len(loc_queue) > 0:
            current = loc_queue.popleft()
            for n in current.neighbors.values():
                if (n.x, n.y) not in basins[basin_loc] and n > current:
                    basins[basin_loc].add((n.x, n.y))
                    loc_queue.append(n)

    sizes = [len(basin) for basin in basins.values()]
    sizes.sort(reverse=True)

    return str(sizes[0] * sizes[1] * sizes[2])


# run_part(part_a, 'a', 2021, 9)
run_part(part_b, 'b', 2021, 9)

