from __future__ import annotations
import heapq
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, Tuple, List, Set

from src.Utility.Movement2d import move


@dataclass
class Passage:

    position: Tuple[int, int]
    value: str


@dataclass
class Path:

    length: int
    end_point: Tuple[int, int]
    keys_found: int

    def add_key(self, key: str):
        key_index = ord(key) - ord('a')
        self.keys_found |= (1 << key_index)

    def has_found_key(self, key: str) -> bool:
        key_index = ord(key) - ord('a')
        return self.keys_found & (1 << key_index) > 0

    def can_open_door(self, door: str) -> bool:
        key = chr(ord(door) + 32)
        return self.has_found_key(key)

    def count_keys(self):
        count = 0
        remaining_keys = self.keys_found
        while remaining_keys > 0:
            count += 1
            remaining_keys = remaining_keys & (remaining_keys - 1)
        return count

    def __lt__(self, other: Path) -> bool:
        return self.length < other.length or (self.length == other.length and self.count_keys() > other.count_keys())


def find_shortest_path(filename: str) -> int:
    input_lines = open(filename).read().splitlines()
    vault: Dict[Tuple[int, int], Passage] = {}
    starting_point: Tuple[int, int] = (0, 0)

    all_keys = 1

    for y in range(len(input_lines)):

        for x in range(len(input_lines[y])):

            coordinate = (x, y)
            v = input_lines[y][x]
            if v != '#':
                vault[coordinate] = Passage(coordinate, v)
                if v == '@':
                    starting_point = coordinate
                elif ord('a') <= ord(v) <= ord('z'):
                    all_keys <<= 1

    paths_to_process: List[Path] = []
    heapq.heappush(paths_to_process, Path(0, starting_point, 0))
    places_seen: Dict[Tuple[int, int], Set[int]] = defaultdict(set)
    all_keys -= 1

    while len(paths_to_process) > 0:
        path = heapq.heappop(paths_to_process)

        loc = path.end_point
        for direction in range(0, 4):
            next_loc = move(loc, direction)
            keys = path.keys_found
            if next_loc in vault and keys not in places_seen[next_loc]:
                passage = vault[next_loc]
                places_seen[next_loc].add(keys)
                if ord('A') <= ord(passage.value) <= ord('Z') and not path.can_open_door(passage.value):
                    # Found a door, but don't have the key
                    continue

                new_path = Path(path.length + 1, next_loc, keys)
                if ord('a') <= ord(passage.value) <= ord('z'):
                    # Found a key
                    new_path.add_key(passage.value)
                    if new_path.keys_found == all_keys:
                        return new_path.length

                heapq.heappush(paths_to_process, new_path)


# assert(find_shortest_path("test1.txt") == 8)
assert(find_shortest_path("test2.txt") == 86)
assert(find_shortest_path("test3.txt") == 132)
assert(find_shortest_path("test4.txt") == 136)
assert(find_shortest_path("test5.txt") == 81)
print("passed tests")
print(find_shortest_path("input.txt"))
