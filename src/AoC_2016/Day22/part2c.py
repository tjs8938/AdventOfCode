from __future__ import annotations

import heapq
import re
from copy import deepcopy
from typing import Tuple, List, Dict

from src.Utility.MatrixPrint import position_to_key, dict_to_matrix, print_matrix
from src.Utility.Movement2d import move


class State:

    def __init__(self, matrix: List[List[Tuple[int, int]]], data_pos: Tuple[int, int]):
        self.matrix = matrix
        self.data_pos: Tuple[int, int] = data_pos
        self.steps = 0

    def __lt__(self, other):
        return (self.steps + self.data_pos[0] + self.data_pos[1]) < (other.steps + other.data_pos[0] + other.data_pos[1])

    def __hash__(self):
        return hash(str(self.matrix))

    def __repr__(self):
        return str(self.data_pos) + " - " + str(self.steps)

    def gen_new_states(self) -> List[State]:
        new_states = []
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                for direction in range(4):
                    new_pos = move((x, y), direction)
                    if 0 <= new_pos[0] < len(self.matrix[y]) and 0 <= new_pos[1] < len(matrix):
                        old_used = self.matrix[y][x][0]
                        new_avail = self.matrix[new_pos[1]][new_pos[0]][1] - self.matrix[new_pos[1]][new_pos[0]][0]
                        new_used = self.matrix[new_pos[1]][new_pos[0]][0]
                        if old_used <= new_avail and new_used == 0:
                            s = State(deepcopy(self.matrix), self.data_pos)
                            s.steps = self.steps + 1
                            s.matrix[y][x] = (0, s.matrix[y][x][1])
                            s.matrix[new_pos[1]][new_pos[0]] = (s.matrix[new_pos[1]][new_pos[0]][0] + old_used, s.matrix[new_pos[1]][new_pos[0]][1])

                            if self.data_pos == (x, y):
                                s.data_pos = new_pos
                            new_states.append(s)
        return new_states


pattern = re.compile("/dev/grid/node-x(?P<x>\\d*)-y(?P<y>\\d*)\\W*(?P<size>\\d*)T\\W*(?P<used>\\d*)T\\W*(?P<avail>\\d*)T")


def node2symbol(used: int) -> str:
    if used == 0:
        return '_'
    elif used > 100:
        return '#'
    else:
        return '.'


# filename = "test1.txt"
filename = "input.txt"
nodes: Dict[str, str] = {}
for input_line in open(filename).read().splitlines():
    m = pattern.match(input_line)
    if m is not None:
        node = m.groupdict()
        node = dict((k, int(v)) for k, v in node.items())
        x, y = node['x'], node['y']
        del node['x']
        del node['y']
        nodes[position_to_key(x, y)] = node2symbol(node["used"])


matrix: List[List[str]] = dict_to_matrix(nodes)
print_matrix(matrix)

# 57 transfers to get the empty space in front of the target data
# 1 more to move the target data left 1 space
# (4 moves to move the empty space to the other side of the target data + 1 move to move the target data) * 28 spaces
# 198 moves total
