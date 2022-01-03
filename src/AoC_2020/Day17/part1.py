from src.Utility.MatrixPrint3d import position_to_key, find_neighboring_positions, dict_to_matrix

STEPS = 6

ACTIVE = '#'
INACTIVE = '.'

# input_file = open("test.txt")
input_file = open("input.txt")
input_lines = input_file.read().splitlines()


class Cube:

    def __init__(self, position: str, state: str):
        self.pos = position
        self.state = state
        self.active_neighbors = 0

    def __repr__(self):
        return self.pos + " - (" + self.state + ", " + str(self.active_neighbors) + ")"


all_cubes = {}
for y in range(len(input_lines)):
    for x in range(len(input_lines[y])):
        pos = position_to_key(x, y, 0)
        all_cubes[pos] = Cube(pos, input_lines[y][x])


def add_inactive_neighbors():
    starting_state = all_cubes.copy()
    for pos, cube in starting_state.items():
        for neighbor in find_neighboring_positions(pos):
            if neighbor not in all_cubes and cube.state == ACTIVE:
                all_cubes[neighbor] = Cube(neighbor, INACTIVE)


def count_neighbors():
    starting_state = all_cubes.copy()
    for pos, cube in starting_state.items():
        neighbor_count = 0
        for neighbor in find_neighboring_positions(pos):
            if neighbor in all_cubes and all_cubes[neighbor].state == ACTIVE:
                neighbor_count += 1

        cube.active_neighbors = neighbor_count


def change_states():
    for cube in all_cubes.values():
        if cube.state == ACTIVE and cube.active_neighbors not in [2, 3]:
            cube.state = INACTIVE
        elif cube.state == INACTIVE and cube.active_neighbors == 3:
            cube.state = ACTIVE


for i in range(STEPS):
    add_inactive_neighbors()
    count_neighbors()
    change_states()

    dict_to_matrix(all_cubes, xform=lambda n: n.state)

count_active = 0
for cube in all_cubes.values():
    if cube.state == ACTIVE:
        count_active += 1

print(count_active)
