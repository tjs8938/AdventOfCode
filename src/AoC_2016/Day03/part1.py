import re

from src.Utility.Movement2d import NORTH, turn, move, move_char

triangles = open("input.txt").read().splitlines()

pattern = re.compile("([0-9]+)")

good_triangles = 0
for line in triangles:
    sides = pattern.findall(line)
    a = int(sides[0])
    b = int(sides[1])
    c = int(sides[2])
    if a + b > c and b + c > a and c + a > b:
        good_triangles += 1

print(good_triangles)