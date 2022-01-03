import re

from src.Utility.Movement2d import NORTH, turn, move

# sequence = "R8, R4, R4, R8"
sequence = open("input.txt").read().splitlines()[0]

pattern = re.compile("([LR])([0-9]*)")

direction = NORTH
position = (0, 0)
visited = []
for moves in pattern.findall(sequence):
    direction = turn(direction, (1 if moves[0] == 'L' else -1) * 90)
    for i in range(int(moves[1])):
        position = move(position, direction)
        if position in visited:
            print(abs(position[0]) + abs(position[1]))
            exit(0)
        else:
            visited.append(position)

