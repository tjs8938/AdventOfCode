#!/bin/python

import re
from pprint import pprint

file = open("input.txt", 'r')
DISTANCE = 10000

pairPattern = re.compile('([0-9]*), ([0-9]*)')

points = []
for line in file.readlines():
    m = pairPattern.match(line)
    point = int(m.group(1)), int(m.group(2))
    points.append(point)

gridx = 0
gridy = 0

for point in points:
    if point[0] > gridx:
        gridx = point[0]

    if point[1] > gridy:
        gridy = point[1]

gridx+=1
gridy+=1
grid = [[-1 for i in range(gridy)] for j in range(gridx)]

for j in range(gridy):
    for i in range(gridx):
        grid[i][j] = []

        for p in range(len(points)):
            point = points[p]
            dist = abs(point[0] - i) + abs(point[1] - j)
            grid[i][j].append(dist)


count = 0
for j in range(gridy):
    for i in range(gridx):
        total = 0
        for p in range(len(points)):
            total += grid[i][j][p]
        if total < DISTANCE:
            count+=1
print (count)
