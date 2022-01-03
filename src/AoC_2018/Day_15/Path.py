from __future__ import annotations
from dataclasses import dataclass
from typing import List

from src.AoC_2018.Day_15.Node import Node


@dataclass
class Path:

    starting_point: Node
    distance: int
    ending_point: Node

    def __lt__(self, other: Path):
        if self.distance < other.distance:
            return True
        elif self.distance == other.distance:
            if self.ending_point < other.ending_point:
                return True
            elif other.ending_point < self.ending_point:
                return False
            else:
                if self.starting_point < other.starting_point:
                    return True
        return False

    def __repr__(self):
        return '(' + str(self.starting_point) + ", " + str(self.distance) + ", " + str(self.ending_point) + ')'

    def get_endpoint(self):
        return self.ending_point

    def get_length(self):
        return self.distance

    def path_to_neighbors(self) -> List[Path]:
        new_paths = []

        for n in self.ending_point.neighbors:
            if n != self.ending_point:
                new_path = Path(self.starting_point, self.distance + 1, n)
                new_paths.append(new_path)

        return new_paths
