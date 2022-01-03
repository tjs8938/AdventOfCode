import re

from src.Utility.Movement2d import NORTH, turn, move

sequence = open("input.txt").read().splitlines()[0]

pattern = re.compile("([LR])([0-9]*)")

direction = NORTH
position = (0, 0)
for moves in pattern.findall(sequence):
    direction = turn(direction, (1 if moves[0] == 'L' else -1) * 90)
    position = move(position, direction, int(moves[1]))

print(abs(position[0]) + abs(position[1]))
