from __future__ import annotations

import itertools
from collections import deque
from dataclasses import dataclass, field
from itertools import count
from typing import Dict, Tuple, List, Deque, Set

from src.Utility.MatrixPrint import print_matrix, tuple_dict_to_matrix
from src.Utility.Movement2d import *


@dataclass
class Passage:
    position: Tuple[int, int]
    value: str
    neighbors: Dict[int, Passage] = field(default_factory=dict, repr=False)

    def add_neighbor(self, neighbor: Passage, direction: int):
        self.neighbors[direction] = neighbor

    def __hash__(self):
        return hash(self.position)

    def __lt__(self, other):
        return self.position < other.position


def find_shortest_path(filename: str) -> int:
    input_lines = open(filename).read().splitlines()
    vault: Dict[Tuple[int, int], Passage] = {}
    portals_to_process: List[Passage] = []

    # Build up the map
    for y in range(len(input_lines)):

        for x in range(len(input_lines[y])):

            coordinate = (x, y)
            v = input_lines[y][x]
            if v not in [' ', '#']:
                new_passage = Passage(coordinate, v)
                vault[coordinate] = new_passage
                if v != '.':
                    portals_to_process.append(new_passage)

                west = move(coordinate, WEST)
                if west in vault:
                    new_passage.add_neighbor(vault[west], WEST)
                    vault[west].add_neighbor(new_passage, EAST)

                north = move(coordinate, NORTH)
                if north in vault:
                    new_passage.add_neighbor(vault[north], NORTH)
                    vault[north].add_neighbor(new_passage, SOUTH)

    starting_point: Tuple[int, int] = (0, 0)
    ending_point: Tuple[int, int] = (0, 0)
    portals_found: Dict[str, Tuple[Passage, int]] = {}

    portals = {}
    # Process the portal spaces
    for p in portals_to_process:
        for direction in range(4):

            # Find a neighbor that is a passage (not part of a portal label)
            if direction in p.neighbors and p.neighbors[direction].value == '.':

                real_passage = p.neighbors[direction]
                if direction == NORTH:
                    portal_code = p.value + p.neighbors[SOUTH].value
                elif direction == EAST:
                    portal_code = p.neighbors[WEST].value + p.value
                elif direction == SOUTH:
                    portal_code = p.neighbors[NORTH].value + p.value
                else:
                    portal_code = p.value + p.neighbors[EAST].value

                del real_passage.neighbors[turn(direction, 180)]

                if portal_code == 'AA':
                    starting_point = real_passage.position
                elif portal_code == 'ZZ':
                    ending_point = real_passage.position
                elif portal_code not in portals_found:
                    portals_found[portal_code] = (real_passage, turn(direction, 180))
                else:
                    other_side = portals_found[portal_code][0]
                    other_side_dir = portals_found[portal_code][1]
                    real_passage.add_neighbor(other_side, turn(direction, 180))
                    other_side.add_neighbor(real_passage, other_side_dir)
                    portals[portal_code] = [real_passage.position, other_side.position]

    # BFS for the shortest path
    current_passages: Set[Passage] = {vault[starting_point]}
    passages_seen: Set[Passage] = {vault[starting_point]}
    debug = True
    for dist in count(1):
        if debug:
            sorted_list = sorted(map(lambda x: x.position, current_passages))
            print(sorted_list)
        neighbors: Set[Passage] = set(filter(lambda n: n not in passages_seen,
                                             itertools.chain.from_iterable([p.neighbors.values()
                                                                            for p in current_passages])))
        if vault[ending_point] in neighbors:
            return dist
        else:
            passages_seen = passages_seen.union(neighbors)
            current_passages = neighbors


# assert(find_shortest_path("test1.txt") == 23)
# assert(find_shortest_path("test2.txt") == 58)
print("Part 1: {}".format(find_shortest_path("input.txt")))

# 719 is too high
