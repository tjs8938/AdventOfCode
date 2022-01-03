#!/bin/python
import re

file = open("input.txt", 'r')

regex = re.compile('([xy])=([0-9]+), ([xy])=([0-9]+)\.\.([0-9]+)')

clay = []

min_x = None
min_y = None
max_x = None
max_y = None

for line in file.readlines():
    m = regex.match(line)
    first = int(m.group(2))
    for second in range(int(m.group(4)), int(m.group(5)) + 1):
        point = None
        if m.group(1) == 'x':
            point = (first, second)
        else:
            point = (second, first)

        clay.append(point)
        if min_x is None or min_x > point[0]:
            min_x = point[0]

        if max_x is None or max_x < point[0]:
            max_x = point[0]

        if min_y is None or min_y > point[1]:
            min_y = point[1]

        if max_y is None or max_y < point[1]:
            max_y = point[1]

min_x -= 1
max_x += 1

scan = [['.' for j in range(min_x, max_x + 1)] for i in range(min_y, max_y + 1)]


def mod_point(x, y, char):
    scan[y - min_y][x - min_x] = char


def get_point(x, y):
    return scan[y - min_y][x - min_x]


for point in clay:
    mod_point(point[0], point[1], '#')

print(min_x, min_y, max_x, max_y)

spillovers = [(500, min_y)]
mod_point(500, min_y, '|')


def fill_side(x, y, shift, edge, char):
    while x + shift != edge and get_point(x + shift, y) != '#':
        x += shift
        mod_point(x, y, char)

        if y < max_y and get_point(x, y + 1) == '.':
            if (x, y) not in spillovers:
                spillovers.append((x, y))
            return False
        elif y >= max_y:
            return False

    if x + shift == edge:
        return False

    return True


def fill_down(x, y):
    while y < max_y and get_point(x, y + 1) == '.':
        y += 1
        mod_point(x, y, '|')

    if y >= max_y or get_point(x, y + 1) == '|':
        return

    left_clay = True
    right_clay = True
    while left_clay and right_clay:
        left_clay = fill_side(x, y, -1, min_x - 1, '|')
        right_clay = fill_side(x, y, 1, max_x + 1, '|')

        if left_clay and right_clay:
            mod_point(x, y, '~')
            left_clay = fill_side(x, y, -1, min_x - 1, '~')
            right_clay = fill_side(x, y, 1, max_x + 1, '~')
            y -= 1
            mod_point(x, y, '|')


while len(spillovers) > 0:
    point = spillovers.pop()
    fill_down(point[0], point[1])

count = 0
for y in scan:
    for x in y:
        if x in ('|', '~'):
            count += 1

print(count)
