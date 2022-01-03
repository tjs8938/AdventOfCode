#!/bin/python
import re
from pprint import pprint

file = open("input.txt", 'r')

regex = re.compile("-?[0-9]+")


class Star:
    def __init__(self, line):
        coords = regex.findall(line)
        self.pos = (int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3]))
        self.neighbors = []

    def distance(self, other):
        dis = abs(self.pos[0] - other.pos[0])
        dis += abs(self.pos[1] - other.pos[1])
        dis += abs(self.pos[2] - other.pos[2])
        dis += abs(self.pos[3] - other.pos[3])
        return dis


stars = []

for line in file.readlines():
    star = Star(line)
    stars.append(star)

for i in range(0, len(stars)):
    for j in range(i+1, len(stars)):
        if stars[i].distance(stars[j]) <= 3:
            stars[i].neighbors.append(stars[j])
            stars[j].neighbors.append(stars[i])

constellations = []


def add_to_const(constellation, star):
    constellation.append(star)
    for neighbor in star.neighbors:
        if neighbor not in constellation:
            add_to_const(constellation, neighbor)


for star in stars:
    foundConst = False
    for constellation in constellations:
        if star in constellation:
            foundConst = True
            break

    if not foundConst:
        constellation = []
        add_to_const(constellation, star)
        constellations.append(constellation)

print(len(constellations))
