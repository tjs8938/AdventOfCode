import re

from src.Utility.MatrixPrint2dHex import MOVES, pair_to_key, find_neighboring_positions, dict_to_matrix

ACTIVE = 1
INACTIVE = 0

# input_file = open("test1.txt")
input_file = open("input.txt")
input_lines = input_file.read().splitlines()

pattern = re.compile("(se|sw|ne|nw|e|w)")

tiles = {}


class Hex:

    def __init__(self, position: str, state: int):
        self.pos = position
        self.state = state
        self.active_neighbors = 0

    def toggle(self):
        self.state = self.state ^ 1

    def __repr__(self):
        return self.pos + " - (" + str(self.state) + ", " + str(self.active_neighbors) + ")"


for line in input_lines:
    position = (0, 0)
    directions = pattern.findall(line)
    for d in directions:
        position = MOVES[d](position)

    key = pair_to_key(position)
    # print(key)
    if key not in tiles:
        tiles[key] = Hex(key, ACTIVE)
    else:
        tiles[key].toggle()

total = 0
for t in tiles.values():
    total += t.state

# print(tiles)
print("Part 1: " + str(total))


def add_inactive_neighbors():
    starting_state = tiles.copy()
    for pos, cube in starting_state.items():
        for neighbor in find_neighboring_positions(pos):
            if neighbor not in tiles and cube.state == ACTIVE:
                tiles[neighbor] = Hex(neighbor, INACTIVE)


def count_neighbors():
    starting_state = tiles.copy()
    for pos, cube in starting_state.items():
        neighbor_count = 0
        for neighbor in find_neighboring_positions(pos):
            if neighbor in tiles and tiles[neighbor].state == ACTIVE:
                neighbor_count += 1

        cube.active_neighbors = neighbor_count


def change_states():
    for cube in tiles.values():
        if cube.state == ACTIVE and cube.active_neighbors not in [1, 2]:
            cube.state = INACTIVE
        elif cube.state == INACTIVE and cube.active_neighbors == 2:
            cube.state = ACTIVE


for i in range(100):
    add_inactive_neighbors()
    count_neighbors()
    change_states()

    # dict_to_matrix(tiles, xform=lambda n: n.state)

total = 0
for tile in tiles.values():
    if tile.state == ACTIVE:
        total += 1

print("Part 1: " + str(total))
