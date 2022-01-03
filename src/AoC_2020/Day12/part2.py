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
# input_file = open("test2.txt")
input_lines = input_file.read().splitlines()

velocity = (10, -1)
position = (0, 0)

pattern = re.compile("([A-Z])([0-9]*)")

for line in input_lines:
    m = pattern.match(line)
    command = m.group(1)
    scale = int(m.group(2))

    if command in DIRECTIONS:
        velocity = move(velocity, DIRECTIONS[command], scale)
    elif command in STEERING:
        if command == 'R':
            scale = 360 - scale

        while scale > 0:
            scale -= 90
            velocity = (velocity[1],
                        velocity[0] * -1)

    else:
        position = (position[0] + (velocity[0] * scale), position[1] + (velocity[1] * scale))

print(position)
print(abs(position[0]) + abs(position[1]))
