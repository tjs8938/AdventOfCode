from __future__ import annotations
from typing import Dict


class Node:
    def __init__(self, x, y, symbol):
        self.symbol = symbol
        self.x = x
        self.y = y
        self.neighbors: Dict[int, Node] = {}

    def __repr__(self):
        return str(self.x) + ',' + str(self.y)

    def set_neighbor(self, n: Node, direction: int):
        self.neighbors[direction] = n

    def get_all_neighbors(self):
        return self.neighbors.values()
