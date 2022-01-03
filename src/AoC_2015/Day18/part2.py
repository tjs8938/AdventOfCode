import itertools
import re
from typing import List

from src.Utility.MatrixPrint import dict_to_matrix, print_matrix
from src.Utility.MatrixPrint2dHex import pair_to_key, key_to_position, def_regex, position_to_key

ACTIVE = 1
INACTIVE = 0

# input_file = open("test2.txt")
# STEPS = 5
input_file = open("input.txt")
STEPS = 100
input_lines = input_file.read().splitlines()

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


class CornerLight(Light):

    def __init__(self, position: str):
        super().__init__(position, ACTIVE)

    def toggle(self):
        pass


MAX_X = len(input_lines[0])
MAX_Y = len(input_lines)

y = 0
for line in input_lines:
    x = 0
    for c in line:
        position = (x, y)
        key = pair_to_key(position)

        if position in [(0, 0), (0, MAX_Y-1), (MAX_X-1, 0), (MAX_X-1, MAX_Y-1)]:
            lights[key] = CornerLight(key)
        else:
            lights[key] = Light(key, ACTIVE if c == '#' else INACTIVE)

        x += 1
    y += 1


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

    # print_matrix(dict_to_matrix(lights, xform=lambda x: '#' if x.state == ACTIVE else '.'))

total = 0
for tile in lights.values():
    if tile.state == ACTIVE:
        total += 1

print("Part 2: " + str(total))
