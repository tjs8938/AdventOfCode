import functools
import itertools
import math
import re


def sum(a, b):
    return abs(a) + abs(b)


class Moon:
    def __init__(self, input_str):
        match = re.match(r'<x=(.*), y=(.*), z=(.*)>', input_str)
        self.pos = (int(match.group(1)), int(match.group(2)), int(match.group(3)))
        self.vel = (0, 0, 0)

    @staticmethod
    def int_comp(a, b):
        if a == b:
            return 0
        elif a < b:
            return -1
        else:
            return 1

    def accel(self, other):
        vx = Moon.int_comp(self.pos[0], other.pos[0])
        vy = Moon.int_comp(self.pos[1], other.pos[1])
        vz = Moon.int_comp(self.pos[2], other.pos[2])

        self.vel = (self.vel[0] - vx, self.vel[1] - vy, self.vel[2] - vz)

    def move(self):
        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1], self.pos[2] + self.vel[2])

    def energy(self):
        print(self.pos, self.vel, functools.reduce(sum, self.pos) * functools.reduce(sum, self.vel))
        return functools.reduce(sum, self.pos) * functools.reduce(sum, self.vel)

    def __str__(self):
        return ("pos=<x={:3}, y={:3}, z={:3}>, vel=<x={:3}, y={:3}, z={:3}>"
                .format(self.pos[0], self.pos[1], self.pos[2],
                        self.vel[0], self.vel[1], self.vel[2]))


file = open('input.txt')
# file = open('test1.txt')
# file = open('test2.txt')
moon_input = file.read().splitlines()

moons = []
for m in moon_input:
    moons.append(Moon(m))

for i in range(0, 1000):

    for pair in itertools.combinations(moons, 2):
        pair[0].accel(pair[1])
        pair[1].accel(pair[0])

    for m in moons:
        m.move()

    print("After {} steps".format(i + 1))
    for m in moons:
        print(m)

print("Total energy: {}".format(functools.reduce(sum, map(lambda x: x.energy(), moons))))
