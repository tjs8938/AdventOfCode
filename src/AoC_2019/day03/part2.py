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

    def __init__(self, pos, segment, distance_from_origin):
        self.distance_from_origin = distance_from_origin
        self.startpoint = pos

        other_end = pos.copy()

        code = segment[0]
        self.length = int(segment[1:])

        self.direction = Direction.VERTICAL if code in ['U', 'D'] else Direction.HORIZONTAL
        mult = 1 if code in ['U', 'R'] else -1

        if self.direction == Direction.VERTICAL:
            other_end.y += mult * self.length
        else:
            other_end.x += mult * self.length

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

    def distance_from_start(self, point):
        return abs(point.x - self.startpoint.x) + abs(point.y - self.startpoint.y)

    def __str__(self):
        return "(%d, %d) - (%d, %d)" % (self.startpoint.x, self.startpoint.y, self.endpoint.x, self.endpoint.y)

    def __repr__(self):
        return self.__str__()


class Intersection:
    def __init__(self, point, wire1, wire2):
        self.point = point
        self.segment1 = wire1
        self.segment2 = wire2

    @staticmethod
    def find_intersection(wire1, wire2):
        h, v = (wire1, wire2) if wire1.direction == Direction.HORIZONTAL else (wire2, wire1)
        intersect = None
        if v.lower().y <= h.lower().y <= v.upper().y and \
                h.lower().x <= v.lower().x <= h.upper().x \
                and [v.lower().x, h.lower().y] != [0, 0]:
            intersect = Intersection(Point(v.lower().x, h.lower().y), wire1, wire2)

        return intersect

    def combined_dist_from_origin(self):
        return self.segment1.distance_from_origin + \
               self.segment2.distance_from_origin + \
               self.segment1.distance_from_start(self.point) + \
               self.segment2.distance_from_start(self.point)


file = open('input.txt')
wires = [[x for x in rec] for rec in csv.reader(file, delimiter=',')]


wire_segments = []

for wire in wires:
    position = Point(0, 0)
    distance_from_origin = 0
    segments = []
    for segment in wire:
        s = Segment(position, segment, distance_from_origin)
        segments.append(s)
        print(s)
        position = s.endpoint
        distance_from_origin += s.length

    wire_segments.append(segments)

segment_pairs = list(pair for pair in itertools.product(wire_segments[0], wire_segments[1]) if pair[0].direction != pair[1].direction)

intersections = []

for pair in segment_pairs:
    horizontal = pair[0] if pair[0].direction == Direction.HORIZONTAL else pair[1]
    vertical = pair[0] if pair[0].direction == Direction.VERTICAL else pair[1]

    i = Intersection.find_intersection(horizontal, vertical)
    if i is not None:
        intersections.append(i)

intersections.sort(key=lambda i: i.combined_dist_from_origin())
print(intersections)
print(len(intersections))
print(intersections[0].combined_dist_from_origin())
