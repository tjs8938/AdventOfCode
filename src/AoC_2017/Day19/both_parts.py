from typing import Tuple, Iterable, Sized

from src.Utility.Movement2d import *


def valid_position(pos: Tuple[int, int], matrix):
    return 0 <= pos[1] < len(matrix) and 0 <= pos[0] < len(matrix[pos[1]])


def look(position, direction, matrix):
    look_space = move(position, direction)
    if not valid_position(look_space, matrix):
        return ''
    return matrix[look_space[1]][look_space[0]]


filename = "input.txt"
# filename = "test1.txt"

routing_diagram = open(filename).read().splitlines()

position = (routing_diagram[0].index('|'), 0)
direction = SOUTH

letters_seen = ''
steps = 1

while True:

    if routing_diagram[position[1]][position[0]] not in ['-', '+', '|']:
        letters_seen += routing_diagram[position[1]][position[0]]

    if valid_position(position, routing_diagram) and look(position, direction, routing_diagram) not in [' ', '']:
        position = move(position, direction)
    else:
        left = turn(direction)
        if valid_position(position, routing_diagram) and look(position, left, routing_diagram) not in [' ', '']:
            direction = left
            position = move(position, direction)
        else:
            right = turn(direction, -90)
            if valid_position(position, routing_diagram) and look(position, right, routing_diagram) not in [' ', '']:
                direction = right
                position = move(position, direction)
            else:
                break
    steps += 1

print(letters_seen)
print(steps)
