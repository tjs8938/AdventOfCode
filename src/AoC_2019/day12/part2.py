import functools
import itertools
import math
import re
from typing import List

X = 0
Y = 1
Z = 2


def sum(a, b):
    return abs(a) + abs(b)


class Moon:
    def __init__(self, input_str):
        match = re.match(r'<x=(.*), y=(.*), z=(.*)>', input_str)
        self.pos = [int(match.group(1)), int(match.group(2)), int(match.group(3))]
        self.vel = [0, 0, 0]
        self.start_pos = self.pos.copy()
        self.start_vel = self.vel.copy()
        print("New Moon: " + str(self.pos))

    @staticmethod
    def int_comp(a, b):
        if a == b:
            return 0
        elif a < b:
            return -1
        else:
            return 1

    def accel(self, other, axis):
        v = Moon.int_comp(self.pos[axis], other.pos[axis])
        self.vel[axis] = self.vel[axis] - v

    def move(self, axis):
        self.pos[axis] = self.pos[axis] + self.vel[axis]

    def energy(self):
        # print(self.pos, self.vel, functools.reduce(sum, self.pos) * functools.reduce(sum, self.vel))
        return functools.reduce(sum, self.pos) * functools.reduce(sum, self.vel)

    def is_start(self, arg):
        return self.pos[arg] == self.start_pos[arg] and self.vel[arg] == self.start_vel[arg]

    def __str__(self):
        return ("pos=<x={:3}, y={:3}, z={:3}>, vel=<x={:3}, y={:3}, z={:3}>"
                .format(self.pos[0], self.pos[1], self.pos[2],
                        self.vel[0], self.vel[1], self.vel[2]))


file = open('input.txt')
# file = open('test1.txt')
# file = open('test2.txt')
moon_input = file.read().splitlines()

moons: List[Moon] = []
for m in moon_input:
    moons.append(Moon(m))

cycles = [0, 0, 0]
i = 0
while any(n == 0 for n in cycles):

    i += 1

    for axis in range(0, 3):
        if cycles[axis] == 0:
            for pair in itertools.combinations(moons, 2):
                pair[0].accel(pair[1], axis)
                pair[1].accel(pair[0], axis)

            for m in moons:
                m.move(axis)

            if all(m.is_start(axis) for m in moons) and cycles[axis] == 0:
                cycles[axis] = i

print(cycles)
# print(math.lcm(cycles[0], cycles[1], cycles[2]))
