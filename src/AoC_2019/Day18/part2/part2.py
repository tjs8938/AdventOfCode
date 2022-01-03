from __future__ import annotations
import heapq
import itertools
from collections import defaultdict, deque
from copy import deepcopy
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Tuple, List, Set, Deque

from src.Utility.MatrixPrint import print_matrix
from src.Utility.Movement2d import move, WEST, NORTH


@dataclass
class Passage:

    position: Tuple[int, int]
    value: str
    neighbors: Dict[Tuple[int, int], Tuple[int, str]]

    @staticmethod
    def link_neighbors(n1: Passage, n2: Passage):

        n1.neighbors[n2.position] = (1, '')
        n2.neighbors[n1.position] = (1, '')


@dataclass
class Path:

    length: int
    end_point: List[Tuple[int, int]]
    keys_found: int
    next_turn: int
    bots_moved: int
    key_order: str

    def add_key(self, key: str):
        if not self.has_found_key(key):
            key_index = ord(key) - ord('a')
            self.keys_found |= (1 << key_index)
            self.key_order += key

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
        return self.length < other.length or \
               (self.length == other.length and len(self.key_order) > len(other.key_order))

    # def print_path_recursive(self, orig: List[str]):
    #     if self.prior_path is not None:
    #         self.prior_path.print_path_recursive(orig)
    #
    #     print("Length {}".format(self.length))
    #     self.print_path(orig)
    #     print()

    def print_path(self, orig: List[str]):
        output: List[str] = []
        out_str = ""
        for y in range(len(orig)):
            for x in range(len(orig[y])):
                c = orig[y][x]
                if (x, y) in self.end_point:
                    out_str += '@'
                elif ord('a') <= ord(c) <= ord('z'):
                    out_str += '.' if self.has_found_key(c) else c
                elif ord('A') <= ord(c) <= ord('Z'):
                    out_str += '.' if self.can_open_door(c) else c
                else:
                    out_str += '#' if c == '#' else '.'
            output.append(out_str)
            out_str = ''

        print_matrix(output)


def find_shortest_path(filename: str) -> int:
    # Parse the passages from the file
    input_lines = open(filename).read().splitlines()
    vault: Dict[Tuple[int, int], Passage] = {}
    starting_path = Path(0, [], 0, 0, 15, '')
    places_seen: Dict[Tuple[Tuple[int, int]], Set[int]] = defaultdict(set)
    passages_to_collapse: Deque[Passage] = deque()

    all_keys = 1

    for y in range(len(input_lines)):

        for x in range(len(input_lines[y])):

            coordinate = (x, y)
            v = input_lines[y][x]
            if v != '#':
                vault[coordinate] = Passage(coordinate, v, {})
                west = move(coordinate, WEST)
                if west in vault:
                    Passage.link_neighbors(vault[west], vault[coordinate])

                north = move(coordinate, NORTH)
                if north in vault:
                    Passage.link_neighbors(vault[north], vault[coordinate])

                if v == '@':
                    starting_path.end_point.append(coordinate)
                elif ord('a') <= ord(v) <= ord('z'):
                    all_keys <<= 1
                else:
                    passages_to_collapse.append(vault[coordinate])

    # Condense the passages until only the starting passages and passages with keys are left
    while len(passages_to_collapse) > 0:
        p = passages_to_collapse.popleft()
        if 0 < len(p.neighbors) <= 2:
            for (n1, n2) in itertools.combinations(p.neighbors, 2):
                neighbor1 = vault[n1]
                neighbor2 = vault[n2]
                dist = p.neighbors[n1][0] + p.neighbors[n2][0]
                reqs = p.neighbors[n1][1] + p.neighbors[n2][1]
                if ord('A') <= ord(p.value) <= ord('Z'):
                    reqs += chr(ord(p.value) + 32)
                neighbor1.neighbors[neighbor2.position] = (dist, reqs)
                neighbor2.neighbors[neighbor1.position] = (dist, reqs)

            for n in p.neighbors:
                neighbor = vault[n]
                del neighbor.neighbors[p.position]
                if len(neighbor.neighbors) == 2 and not ord('a') <= ord(neighbor.value) <= ord('z') and neighbor.value != '@':
                    passages_to_collapse.append(neighbor)
            p.neighbors.clear()

    paths_to_process: List[Path] = []
    heapq.heappush(paths_to_process, starting_path)
    places_seen[tuple(starting_path.end_point)].add(0)

    all_keys -= 1

    while len(paths_to_process) > 0:
        path = heapq.heappop(paths_to_process)
        bot = path.next_turn
        loc = path.end_point[bot]

        for next_loc in vault[loc].neighbors:
            new_endpoints = deepcopy(path.end_point)
            new_endpoints[bot] = next_loc
            new_endpoints_tuple = tuple(new_endpoints)
            keys = path.keys_found
            if keys not in places_seen[new_endpoints_tuple]:
                passage = vault[next_loc]
                places_seen[new_endpoints_tuple].add(keys)
                if any(not path.has_found_key(key) for key in passage.neighbors[loc][1]):
                    # not all of the necessary keys have been found
                    continue

                bots_moved = path.bots_moved | (1 << bot)
                new_path = Path(path.length + passage.neighbors[loc][0], new_endpoints, keys, (path.next_turn + 1) % 4,
                                bots_moved, path.key_order)
                if ord('a') <= ord(passage.value) <= ord('z'):
                    # Found a key
                    new_path.add_key(passage.value)
                    if new_path.keys_found == all_keys:
                        # new_path.print_path_recursive(input_lines)
                        return new_path.length

                heapq.heappush(paths_to_process, new_path)

        # This bot may be done or stuck at a door, add a path that proceeds to the next bot
        bots_moved = path.bots_moved & (15 - (1 << bot))

        # Don't push the path if no bot has moved in a full cycle
        if bots_moved > 0:
            new_path = Path(path.length, deepcopy(path.end_point), path.keys_found, (path.next_turn + 1) % 4,
                            bots_moved, path.key_order)
            heapq.heappush(paths_to_process, new_path)


assert(find_shortest_path("test1.txt") == 8)
assert(find_shortest_path("test2.txt") == 24)
assert(find_shortest_path("test3.txt") == 32)
assert(find_shortest_path("test4.txt") == 72)
print("passed tests")
start_time = datetime.now()
print(find_shortest_path("input.txt"))
print(datetime.now() - start_time)
