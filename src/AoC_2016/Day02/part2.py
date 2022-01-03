import re

from src.Utility.Movement2d import NORTH, turn, move, move_char

codes = open("input.txt").read().splitlines()

keypad = {
    (0, 2): "5",
    (1, 1): "2",
    (1, 2): "6",
    (1, 3): "A",
    (2, 0): "1",
    (2, 1): "3",
    (2, 2): "7",
    (2, 3): "B",
    (2, 4): "D",
    (3, 1): "4",
    (3, 2): "8",
    (3, 3): "C",
    (4, 2): "9",
}

position = (1, 1)

for line in codes:
    for c in line:
        next_pos = move_char(position, c)
        if next_pos in keypad:
            position = next_pos

    print(keypad[position])
