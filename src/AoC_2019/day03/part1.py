import csv
import itertools
from enum import IntEnum, auto


class Direction(IntEnum):
    HORIZONTAL = 0
    VERTICAL = 1


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __copy__(self):
        return Point(self.x, self.y)

    def copy(self):
        return self.__copy__()


class Segment:

    def __init__(self, pos, seg):
        self.startpoint = pos

        other_end = pos.copy()

        code = segment[0]
        dist = int(segment[1:])

        self.direction = Direction.VERTICAL if code in ['U', 'D'] else Direction.HORIZONTAL
        mult = 1 if code in ['U', 'R'] else -1

        if self.direction == Direction.VERTICAL:
            other_end.y += mult * dist
        else:
            other_end.x += mult * dist

        self.endpoint = other_end

    def lower(self):
        if self.startpoint.x <= self.endpoint.x and self.startpoint.y <= self.endpoint.y:
            return self.startpoint
        else:
            return self.endpoint

    def upper(self):
        if self.startpoint.x <= self.endpoint.x and self.startpoint.y <= self.endpoint.y:
            return self.endpoint
        else:
            return self.startpoint

    def __str__(self):
        return "(%d, %d) - (%d, %d)" % (self.startpoint.x, self.startpoint.y, self.endpoint.x, self.endpoint.y)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def find_intersection(h, v):
        intersect = None
        if v.lower().y <= h.lower().y <= v.upper().y and \
                h.lower().x <= v.lower().x <= h.upper().x \
                and [v.lower().x, h.lower().y] != [0, 0]:
            intersect = [v.lower().x, h.lower().y]

        return intersect


file = open('input.txt')
wires = [[x for x in rec] for rec in csv.reader(file, delimiter=',')]


wire_segments = []

for wire in wires:
    position = Point(0, 0)
    segments = []
    for segment in wire:
        s = Segment(position, segment)
        segments.append(s)
        print(s)
        position = s.endpoint

    wire_segments.append(segments)

segment_pairs = list(pair for pair in itertools.product(wire_segments[0], wire_segments[1]) if pair[0].direction != pair[1].direction)

intersections = []

for pair in segment_pairs:
    horizontal = pair[0] if pair[0].direction == Direction.HORIZONTAL else pair[1]
    vertical = pair[0] if pair[0].direction == Direction.VERTICAL else pair[1]

    i = Segment.find_intersection(horizontal, vertical)
    if i is not None:
        intersections.append(i)

intersections.sort(key=lambda point: abs(point[0]) + abs(point[1]))
print(intersections)
print(intersections[0])
