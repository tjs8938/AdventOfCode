from typing import Dict, Set


class House:
    def __init__(self, house_num):
        self.house_num = house_num
        self.neighbors: Set[House] = set()

        self.dist_to_loc: Dict[str, int] = {house_num: 0}

    def set_dist(self, location: str, dist: int):
        self.dist_to_loc[location] = dist

    @staticmethod
    def link_neighbors(a, b):
        a.neighbors.add(b)
        b.neighbors.add(a)

