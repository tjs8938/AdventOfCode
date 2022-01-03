from __future__ import annotations

import heapq
import itertools
from dataclasses import dataclass
from pprint import pprint

from aocd.transforms import lines

from src.Utility.MatrixPrint import position_to_key
from src.Utility.NodeMap.NodeMap import NodeMap
from src.aoc_frame import run_part

from typing import Dict, Tuple


class Node:
    def __init__(self, x, y, symbol):
        self.symbol = symbol
        self.x = x
        self.y = y
        self.neighbors: Dict[int, Node] = {}

    def __repr__(self):
        return str(self.x) + ',' + str(self.y)

    def set_neighbor(self, n: Node, direction: int):
        self.neighbors[direction] = n

    def get_all_neighbors(self):
        return self.neighbors.values()


@dataclass
class Path:
    end_loc: Node
    cost: int

    def __lt__(self, other):
        return self.cost < other.cost


def part_a(input_data: str) -> str:
    in_lines = lines(input_data)
    risk_levels = NodeMap(in_lines, Node)

    start = Path(risk_levels.nodes[position_to_key(0, 0)], 0)
    path_heap = [start]

    cheapest_to_node: Dict[Tuple[int, int], int] = {(0, 0): 0}

    while len(path_heap) > 0:
        current_path = heapq.heappop(path_heap)
        for neighbor in current_path.end_loc.neighbors.values():
            new_path = Path(neighbor, current_path.cost + int(neighbor.symbol))
            n_loc = (neighbor.x, neighbor.y)
            if n_loc == (len(in_lines[0]) - 1, len(in_lines) - 1):
                return str(new_path.cost)
            else:
                if n_loc in cheapest_to_node and cheapest_to_node[n_loc] <= new_path.cost:
                    continue
                cheapest_to_node[n_loc] = new_path.cost
                heapq.heappush(path_heap, new_path)
    return 'A'


def part_b(input_data: str) -> str:
    in_lines = lines(input_data)
    starting_lines = lines(input_data)
    # Duplicate the input
    for diagonal in range(1, 9):
        for x, y in itertools.product(range(5), repeat=2):
            if x + y == diagonal:
                for i in range(len(starting_lines)):
                    line = starting_lines[i]
                    append_line = "".join([str(int(x) + diagonal - 9 if int(x) + diagonal > 9 else int(x) + diagonal) for x in line])
                    if x == 0:
                        in_lines.append(append_line)
                    else:
                        in_lines[len(starting_lines) * y + i] += append_line

    # pprint(in_lines)
    # return 'B'
    risk_levels = NodeMap(in_lines, Node)

    start = Path(risk_levels.nodes[position_to_key(0, 0)], 0)
    path_heap = [start]

    cheapest_to_node: Dict[Tuple[int, int], int] = {(0, 0): 0}

    while len(path_heap) > 0:
        current_path = heapq.heappop(path_heap)
        for neighbor in current_path.end_loc.neighbors.values():
            new_path = Path(neighbor, current_path.cost + int(neighbor.symbol))
            n_loc = (neighbor.x, neighbor.y)
            if n_loc == (len(in_lines[0]) - 1, len(in_lines) - 1):
                return str(new_path.cost)
            else:
                if n_loc in cheapest_to_node and cheapest_to_node[n_loc] <= new_path.cost:
                    continue
                cheapest_to_node[n_loc] = new_path.cost
                heapq.heappush(path_heap, new_path)
    return 'B'


# run_part(part_a, 'a', 2021, 15)
run_part(part_b, 'b', 2021, 15)

