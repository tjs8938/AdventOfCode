#!/bin/python

import re
from pprint import pprint

file = open("input.txt", 'r')

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
        shortestPoint = -1
        shortestDistance = gridx + gridy + 1

        for p in range(len(points)):
            point = points[p]
            dist = abs(point[0] - i) + abs(point[1] - j)
            if dist == shortestDistance:
                shortestPoint = -1
                shortestDistance = dist

            elif dist < shortestDistance:
                shortestPoint = p
                shortestDistance = dist

        grid[i][j] = shortestPoint


pointCounts = {}
for j in range(gridy):
    for i in range(gridx):
        if grid[i][j] == -1:
            continue

        key = str(grid[i][j])

        if key not in pointCounts:
            pointCounts[key] = 0

        if pointCounts[key] == -1:
            continue

        if i == 0 or j == 0 or i == gridx-1 or j == gridy-1:
            pointCounts[key] = -1
        else:
            pointCounts[key] += 1

highestCount = 0
highestPoint = ""
for key in pointCounts:
    if pointCounts[key] > highestCount:
        highestCount = pointCounts[key]
        highestPoint = key

print(highestCount)
