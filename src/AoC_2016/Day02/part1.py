import re

from src.Utility.Movement2d import NORTH, turn, move, move_char

codes = open("input.txt").read().splitlines()

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

position = (1, 1)

for line in codes:
    for c in line:
        next_pos = move_char(position, c)
        if 0 <= next_pos[0] <= 2 and 0 <= next_pos[1] <= 2:
            position = next_pos

    print(keypad[position[1]][position[0]])
