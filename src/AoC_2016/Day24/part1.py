from typing import Dict, List

from src.AoC_2016.Day24.Node import Node
from src.Utility.MatrixPrint import position_to_key

# filename = "test1.txt"
filename = "input.txt"

nodes: Dict[str, Node] = {}
locations: Dict[str, Node] = {}

input_lines = open(filename).read().splitlines()
for y in range(len(input_lines)):
    for x in range(len(input_lines[y])):
        symbol = input_lines[y][x]
        if symbol != '#':
            n = Node(x, y)
            nodes[position_to_key(x, y)] = n

            if symbol != '.':
                n.set_dist(symbol, 0)
                locations[symbol] = n

            west_neighbor_key = position_to_key(x - 1, y)
            north_neighbor_key = position_to_key(x, y - 1)

            if west_neighbor_key in nodes:
                Node.link_neighbors(n, nodes[west_neighbor_key])
            if north_neighbor_key in nodes:
                Node.link_neighbors(n, nodes[north_neighbor_key])

nodes_to_process: List[Node] = list(locations.values())
while len(nodes_to_process) > 0:
    process = nodes_to_process.pop(0)
    for neighbor in process.neighbors:
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

    for loc in locations:
        if loc not in visited:
            new_path = visited + loc
            path_len = length + locations[current].dist_to_loc[loc]
            if len(new_path) == len(locations) and path_len < best_yet:
                best_yet = path_len
            elif path_len < best_yet:
                travel(new_path, loc, path_len)


travel('0', '0', 0)

print(best_yet)