from typing import Dict, List


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors: List[Node] = []

        self.dist_to_loc: Dict[str, int] = {}

    def __repr__(self):
        return str(self.x) + ',' + str(self.y)

    def set_dist(self, location: str, dist: int):
        self.dist_to_loc[location] = dist

    @staticmethod
    def link_neighbors(a, b):
        a.neighbors.append(b)
        b.neighbors.append(a)

