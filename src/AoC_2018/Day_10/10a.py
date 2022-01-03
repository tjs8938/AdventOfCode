#!/bin/python
import re
import time
from functools import reduce
from pprint import pprint

file = open("input.txt", 'r')
pattern = re.compile("[0-9-]+")


class Star:

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def __lt__(self, other):
        return self.y < other.y or (self.y == other.y and self.x < other.x)

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def inc(self):
        self.x += self.vx
        self.y += self.vy


def printStars(stars):
    index = 0
    print()
    print()
    min_x = stars[0].x
    min_y = stars[0].y
    max_x = stars[0].x
    max_y = stars[0].y

    for s in stars:
        if min_x > s.x:
            min_x = s.x
        if min_y > s.y:
            min_y = s.y
        if max_x < s.x:
            max_x = s.x
        if max_y < s.y:
            max_y = s.y

    for y in range(min_y, max_y):
        row = ""
        for x in range(min_x, max_x):
            char = '.'
            if stars[index].x == x and stars[index].y == y:
                char = '#'
                if index < len(stars)-1:
                    index += 1
            row += char

        print(row)

def incStars():
    for s in stars:
        s.inc()
    stars.sort()


stars = []
for line in file.readlines():
    m = pattern.findall(line)
    stars.append(Star(int(m[0]), int(m[1]), int(m[2]), int(m[3])))

secs = 0
min_area = 10000000
while True:

    # printStars(stars)
    print(secs)
    incStars()
    # print(reduce(lambda x, y: Star(abs(x.x) + abs(x.y), abs(y.x) + abs(y.y), 0, 0), stars))
    # time.sleep(1)
    secs += 1
    if 10100 < secs < 10300:
        # min_x = stars[0].x
        # min_y = stars[0].y
        # max_x = stars[0].x
        # max_y = stars[0].y
        #
        # for s in stars:
        #     if min_x > s.x:
        #         min_x = s.x
        #     if min_y > s.y:
        #         min_y = s.y
        #     if max_x < s.x:
        #         max_x = s.x
        #     if max_y < s.y:
        #         max_y = s.y
        #
        # area = (max_x - min_x) * (max_y - min_y)
        # if area < min_area:
        #     min_area = area
        #     print(secs, min_area)
        #     if secs == 10135:
        printStars(stars)
        # time.sleep(15)

