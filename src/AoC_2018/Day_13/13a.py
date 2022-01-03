#!/bin/python
from pprint import pprint

file = open("input.txt", 'r')

LEFT = -1
RIGHT = 1

NORTH = (0, -1)
EAST = (-1, 0)
SOUTH = (0, 1)
WEST = (1, 0)

DIRECTIONS = [NORTH, WEST, SOUTH, EAST]

CAR_SYMBOLS = ['^', '>', 'v', '<']

TURNS = [
    {'/': RIGHT, '\\': LEFT},
    {'/': LEFT, '\\': RIGHT},
    {'/': RIGHT, '\\': LEFT},
    {'/': LEFT, '\\': RIGHT}
         ]

map_dirs = dict(zip(CAR_SYMBOLS, range(len(CAR_SYMBOLS))))

class Road:
    def __init__(self, char, car):
        self.char = char
        self.car = car

    def __repr__(self):
        return self.char

class Car:
    def __init__(self, x, y, direction):
        self.direction = direction
        self.y = y
        self.x = x
        self.intersections = 0

    def __lt__(self, other):
        return self.y < other.y or (self.y == other.x and self.x < other.x)

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ') - ' + str(self.direction)


roads = []
cars = []
x = 0
y = 0
for line in file.readlines():
    roads.append([])
    for char in line:
        car = None
        if char in CAR_SYMBOLS:
            car = Car(x, y, map_dirs[char])
            cars.append(car)
            if char in ['<', '>']:
                char = '-'
            else:
                char = '|'

        roads[y].append(Road(char, car))
        x += 1

    y += 1
    x = 0

while True:
    cars.sort()
    for car in cars:
        print(car)
        roads[car.y][car.x].car = None
        car.x += DIRECTIONS[car.direction][0]
        car.y += DIRECTIONS[car.direction][1]
        road = roads[car.y][car.x]
        if road.car is not None:
            print(car.x, car.y)
            exit(0)

        road.car = car
        if road.char == '+':
            direction = 0
            if car.intersections % 3 == 0:
                direction = LEFT
            elif car.intersections % 3 == 2:
                direction = RIGHT

            car.intersections += 1
            car.direction = (car.direction + direction) % 4
        if road.char in ['/', '\\']:
            car.direction = (car.direction + TURNS[car.direction][road.char]) % 4




