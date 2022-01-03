from functools import reduce

from src.Utility.MatrixPrint import flip_vertical, flip_horizontal, rotate_right, rotate_left
from src.Utility.Movement2d import NORTH, SOUTH, WEST, EAST


class Segment:

    def __init__(self, tile_num):
        self.tile_num = tile_num
        self.rows = []
        self.legal_neighbors = {}
        self.neighbor_orientation = [None, None, None, None]
        self.left = ""
        self.right = ""

    def add_row(self, row):
        self.rows.append(row)
        self.left += row[0]
        self.right += row[-1]

    def get_left(self):
        return reduce(lambda a, b: a + b, map(lambda row: row[0], self.rows[::-1]))

    def get_right(self):
        return reduce(lambda a, b: a + b, map(lambda row: row[-1], self.rows))

    def get_bottom(self):
        return self.rows[-1][::-1]

    def get_top(self):
        return self.rows[0]

    def get_all_sides(self):
        return [self.get_top(), self.get_left(), self.get_bottom(), self.get_right()]

    def check_neighborliness(self, other):
        for idx in range(len(self.get_all_sides())):
            for other_idx in range(len(other.get_all_sides())):
                if self.get_all_sides()[idx] == other.get_all_sides()[other_idx] or \
                        self.get_all_sides()[idx] == other.get_all_sides()[other_idx][::-1]:
                    self.legal_neighbors[other.tile_num] = other
                    other.legal_neighbors[self.tile_num] = self
                    self.neighbor_orientation[idx] = other
                    other.neighbor_orientation[other_idx] = self

    def __lt__(self, other):
        return len(self.legal_neighbors) < len(other.legal_neighbors)

    def __repr__(self):
        return self.tile_num + ": " + str(self.legal_neighbors.keys())

    def flip_vertical(self):
        self.rows = flip_vertical(self.rows)
        t = self.neighbor_orientation[NORTH]
        self.neighbor_orientation[NORTH] = self.neighbor_orientation[SOUTH]
        self.neighbor_orientation[SOUTH] = t

    def flip_horizontal(self):
        self.rows = flip_horizontal(self.rows)
        t = self.neighbor_orientation[WEST]
        self.neighbor_orientation[WEST] = self.neighbor_orientation[EAST]
        self.neighbor_orientation[EAST] = t

    def rotate_left(self):
        self.rows = rotate_left(self.rows)
        t = self.neighbor_orientation[:-1]
        self.neighbor_orientation = [self.neighbor_orientation[3]]
        self.neighbor_orientation.extend(t)

    def rotate_right(self):
        self.rows = rotate_right(self.rows)
        t = self.neighbor_orientation[0]
        self.neighbor_orientation = self.neighbor_orientation[1:]
        self.neighbor_orientation.append(t)