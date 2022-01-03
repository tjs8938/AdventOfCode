import re

from src.Utility.Movement2d import move, turn

NORTH = 0
WEST = 1
SOUTH = 2
EAST = 3

LEFT = 1
RIGHT = -1

DIRECTIONS = {'N': NORTH, 'W': WEST, 'S': SOUTH, 'E': EAST}
STEERING = {'L': LEFT, 'R': RIGHT}

input_file = open("input.txt")
# input_file = open("test1.txt")
input_lines = input_file.read().splitlines()

current_direction = EAST
position = (0, 0)

pattern = re.compile("([A-Z])([0-9]*)")

for line in input_lines:
    m = pattern.match(line)
    command = m.group(1)
    scale = int(m.group(2))

    if command in DIRECTIONS:
        position = move(position, DIRECTIONS[command], scale)
    elif command in STEERING:
        current_direction = turn(current_direction, STEERING[command] * scale)
    else:
        position = move(position, current_direction, scale)

print(position)
print(abs(position[0]) + abs(position[1]))
