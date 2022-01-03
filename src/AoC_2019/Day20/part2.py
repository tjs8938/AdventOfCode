from __future__ import annotations

import itertools
from dataclasses import dataclass, field
from itertools import count
from typing import Dict, Tuple, List, Set

from src.Utility.MatrixPrint import print_matrix
from src.Utility.Movement2d import *


@dataclass
class Passage:
    position: Tuple[int, int]
    value: str
    neighbors: Dict[int, Tuple[Passage, int]] = field(default_factory=dict, repr=False)

    def add_neighbor(self, neighbor: Passage, direction: int, level_change: int = 0):
        self.neighbors[direction] = (neighbor, level_change)

    def get_neighbors(self, current_level) -> Set[Tuple[Passage, int]]:
        return set(filter(lambda x: x[1] >= 0, map(lambda n: (n[0], current_level + n[1]), self.neighbors.values())))

    def __hash__(self):
        return hash(self.position)


def print_steps(maze: List[str], locations: Set[Tuple[Passage, int]]):
    matrix = []
    for y in range(len(maze)):
        matrix.append([])
        for x in range(len(maze[y])):
            matrix[y].append(maze[y][x])

    for p in locations:
        loc = p[0].position
        matrix[loc[1]][loc[0]] = '\x1b[31m' + str(p[1]) + '\x1b[0m'
    print_matrix(matrix)


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

    max_x = max(map(lambda x: x.position[0], filter(lambda y: y.value == '.', vault.values())))
    max_y = max(map(lambda x: x.position[1], filter(lambda y: y.value == '.', vault.values())))

    portals = {}
    # Process the portal spaces
    for p in portals_to_process:
        for direction in range(4):

            # Find a neighbor that is a passage (not part of a portal label)
            if direction in p.neighbors and p.neighbors[direction][0].value == '.':

                real_passage = p.neighbors[direction][0]
                if direction == NORTH:
                    portal_code = p.value + p.neighbors[SOUTH][0].value
                elif direction == EAST:
                    portal_code = p.neighbors[WEST][0].value + p.value
                elif direction == SOUTH:
                    portal_code = p.neighbors[NORTH][0].value + p.value
                else:
                    portal_code = p.value + p.neighbors[EAST][0].value

                del real_passage.neighbors[turn(direction, 180)]

                if portal_code == 'AA':
                    starting_point = real_passage.position
                elif portal_code == 'ZZ':
                    ending_point = real_passage.position
                elif portal_code not in portals_found:
                    portals_found[portal_code] = (real_passage, turn(direction, 180))
                else:
                    outer_edge = -1 if (real_passage.position[0] in [2, max_x] or
                                        real_passage.position[1] in [2, max_y]) else 1

                    other_side = portals_found[portal_code][0]
                    other_side_dir = portals_found[portal_code][1]
                    real_passage.add_neighbor(other_side, turn(direction, 180), outer_edge)
                    other_side.add_neighbor(real_passage, other_side_dir, outer_edge * -1)
                    portals[portal_code] = [real_passage.position, other_side.position]

    current_passages: Set[Tuple[Passage, int]] = {(vault[starting_point], 0)}
    passages_seen: Set[Tuple[Passage, int]] = {(vault[starting_point], 0)}
    for dist in count(1):
        neighbors: Set[Tuple[Passage, int]] = set(filter(lambda n: n not in passages_seen,
                                                         itertools.chain.from_iterable([p[0].get_neighbors(p[1])
                                                                                        for p in current_passages])))
        if (vault[ending_point], 0) in neighbors:
            return dist
        else:
            passages_seen = passages_seen.union(neighbors)
            current_passages = neighbors

        # print(dist)
        # print_steps(input_lines, current_passages)


assert (find_shortest_path("test1.txt") == 26)
assert (find_shortest_path("test3.txt") == 396)
print("Part 2: {}".format(find_shortest_path("input.txt")))

