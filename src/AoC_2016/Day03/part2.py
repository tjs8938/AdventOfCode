import re

from src.Utility.Movement2d import NORTH, turn, move, move_char

triangles = open("input.txt").read().splitlines()

pattern = re.compile("([0-9]+)")

all_sides = []
for line in triangles:
    sides = list(map(lambda x: int(x), pattern.findall(line)))
    all_sides.append(sides)

good_triangles = 0
for i in range(0, len(all_sides), 3):
    for j in range(len(all_sides[i])):
        a = all_sides[i][j]
        b = all_sides[i+1][j]
        c = all_sides[i+2][j]
        if a + b > c and b + c > a and c + a > b:
            good_triangles += 1

print(good_triangles)