NORTH = 0
WEST = 1
SOUTH = 2
EAST = 3
NE = 4
NW = 5
SE = 6
SW = 7

NUM_CARD_DIRS = 4
NUM_ALL_DIRS = 8

CHAR_MOVEMENTS = {'>': EAST, '<': WEST, 'v': SOUTH, '^': NORTH, 'R': EAST, 'L': WEST, 'D': SOUTH, 'U': NORTH}

MOVE = [
    lambda x, spaces: (x[0], x[1] - spaces),
    lambda x, spaces: (x[0] - spaces, x[1]),
    lambda x, spaces: (x[0], x[1] + spaces),
    lambda x, spaces: (x[0] + spaces, x[1]),
    lambda x, spaces: move(move(x, NORTH, spaces), EAST, spaces),
    lambda x, spaces: move(move(x, NORTH, spaces), WEST, spaces),
    lambda x, spaces: move(move(x, SOUTH, spaces), EAST, spaces),
    lambda x, spaces: move(move(x, SOUTH, spaces), WEST, spaces)
]


def move(position, direction, spaces=1):
    return MOVE[direction](position, spaces)


def move_char(position, direction):
    return MOVE[CHAR_MOVEMENTS[direction]](position, 1)


def turn(current, degrees=90):
    degrees = degrees % 360

    while degrees > 0:
        degrees -= 90
        current = (current + 1) % 4

    return current

