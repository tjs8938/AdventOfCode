import itertools
import re
from typing import List

from src.Utility.MatrixPrint2dHex import pair_to_key, key_to_position, def_regex, position_to_key

ACTIVE = 1
INACTIVE = 0

input_file = open("test1.txt")
STEPS = 4
# input_file = open("input.txt")
# STEPS = 100
input_lines = input_file.read().splitlines()

pattern = re.compile("(se|sw|ne|nw|e|w)")

lights = {}


class Light:

    def __init__(self, position: str, state: int):
        self.pos = position
        self.state = state
        self.active_neighbors = 0

    def toggle(self):
        self.state = self.state ^ 1

    def __repr__(self):
        return self.pos + " - (" + str(self.state) + ", " + str(self.active_neighbors) + ")"


y = 0
for line in input_lines:
    x = 0
    for c in line:
        position = (x, y)
        key = pair_to_key(position)
        lights[key] = Light(key, ACTIVE if c == '#' else INACTIVE)

        x += 1
    y += 1

MAX_X = len(input_lines[0])
MAX_Y = len(input_lines)
# def add_inactive_neighbors():
#     starting_state = lights.copy()
#     for pos, cube in starting_state.items():
#         for neighbor in find_neighboring_positions(pos):
#             if neighbor not in lights and cube.state == ACTIVE:
#                 lights[neighbor] = Light(neighbor, INACTIVE)


def find_neighboring_positions(pos: str) -> List[str]:
    x, y = key_to_position(pos, def_regex)
    offsets = [-1, 0, 1]
    offset_combos = itertools.product(offsets, repeat=2)
    neighboring_positions = []
    for combo in offset_combos:
        if combo[0] != 0 or combo[1] != 0:
            px = x + combo[0]
            py = y + combo[1]
            if 0 <= px < MAX_X and 0 <= py < MAX_Y:
                neighboring_positions.append(position_to_key(px, py))

    return neighboring_positions


def count_neighbors():
    starting_state = lights.copy()
    for pos, cube in starting_state.items():
        neighbor_count = 0
        for neighbor in find_neighboring_positions(pos):
            if neighbor in lights and lights[neighbor].state == ACTIVE:
                neighbor_count += 1

        cube.active_neighbors = neighbor_count


def change_states():
    for cube in lights.values():
        if cube.state == ACTIVE and cube.active_neighbors not in [3, 2]:
            cube.toggle()
        elif cube.state == INACTIVE and cube.active_neighbors == 3:
            cube.toggle()


for i in range(STEPS):
    count_neighbors()
    change_states()

    # dict_to_matrix(tiles, xform=lambda n: n.state)

total = 0
for tile in lights.values():
    if tile.state == ACTIVE:
        total += 1

print("Part 1: " + str(total))
