from __future__ import annotations
from typing import Dict, List

from src.Utility.NodeMap.NodeMap import NodeMap


class Day24Node:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.neighbors: Dict[int, Day24Node] = {}

        self.dist_to_loc: Dict[str, int] = {}

    def __repr__(self):
        return str(self.x) + ',' + str(self.y)

    def set_neighbor(self, n: Day24Node, direction: int):
        self.neighbors[direction] = n

    def get_all_neighbors(self):
        return self.neighbors.values()


filename = "input.txt"

input_lines = open(filename).read().splitlines()
node_map = NodeMap[Day24Node](input_lines, node_gen=Day24Node)

for loc, node in node_map.locations.items():
    node.dist_to_loc[loc] = 0

nodes_to_process: List[Day24Node] = list(node_map.locations.values())
while len(nodes_to_process) > 0:
    process = nodes_to_process.pop(0)
    for neighbor in process.neighbors.values():
        changed = False
        for loc, dist in process.dist_to_loc.items():
            if loc not in neighbor.dist_to_loc or neighbor.dist_to_loc[loc] > dist + 1:
                neighbor.dist_to_loc[loc] = dist + 1
                changed = True

        if changed:
            nodes_to_process.append(neighbor)


best_yet = pow(2, 31)


def travel(visited: str, current: str, length: int):
    global best_yet

    for loc in node_map.locations:
        if loc not in visited:
            new_path = visited + loc
            path_len = length + node_map.locations[current].dist_to_loc[loc]
            if len(new_path) == len(node_map.locations) and path_len < best_yet:
                best_yet = path_len
            elif path_len < best_yet:
                travel(new_path, loc, path_len)


travel('0', '0', 0)

print(best_yet)
