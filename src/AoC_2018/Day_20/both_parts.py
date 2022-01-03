from __future__ import annotations

import collections
from copy import deepcopy
from typing import Dict, Tuple, List, Deque, Set

from src.Utility.MatrixPrint import position_to_key, pair_to_key
from src.Utility.Movement2d import *

DIRECTIONS = {'N': NORTH, 'E': EAST, 'W': WEST, 'S': SOUTH}


class Room:

    def __init__(self, position: Tuple[int, int], base: BaseMap):
        self.position: Tuple[int, int] = position
        self.base: BaseMap = base
        self.neighbors: Dict[str, Room] = {}

    def get_neighbor(self, direction) -> Tuple[int, int]:
        if direction not in self.neighbors:
            new_pos = move(self.position, direction)
            new_room = Room(new_pos, self.base)
            new_room.neighbors[(direction + 2) % 4] = self
            self.neighbors[direction] = new_room
            self.base.rooms[pair_to_key(new_pos)] = new_room

        return self.neighbors[direction].position

    def __repr__(self):
        return str(self.position) + ", " + str(len(self.neighbors))


class BaseMap:

    def __init__(self, path: str):
        self.dist_to_room: Dict[str, int] = {position_to_key(0, 0): 0}
        self.rooms: Dict[str, Room] = {position_to_key(0, 0): Room((0, 0), self)}
        self.path = path

    def new_process_path(self, start_positions: Set[Tuple[int, int]], start_index) -> Tuple[Set[Tuple[int, int]], int]:
        index = start_index
        positions = deepcopy(start_positions)
        end_positions: Set[Tuple[int, int]] = set()
        while index < len(self.path):
            next_char = self.path[index]
            if next_char in ['N', 'E', 'S', 'W']:
                direction = DIRECTIONS[next_char]
                temp_positions: Set[Tuple[int, int]] = set()
                for p in positions:
                    temp_positions.add(self.rooms[pair_to_key(p)].get_neighbor(direction))
                positions = temp_positions
            elif next_char == '|':
                end_positions.update(positions)
                positions = deepcopy(start_positions)
            elif next_char == '(':
                positions, index = self.new_process_path(positions, index + 1)
            else:
                end_positions.update(positions)
                return end_positions, index
            index += 1

    # def process_path(self, position: Tuple[int, int], path: str):
    #     # print(position, path)
    #     current_room = self.rooms[pair_to_key(position)]
    #
    #     index = 0
    #     while index < len(path) and path[index] in ['N', 'E', 'S', 'W']:
    #         direction = DIRECTIONS[path[index]]
    #         current_room = current_room.get_neighbor(direction)
    #
    #         index += 1
    #
    #     # print(current_room)
    #     # print(path[index:])
    #
    #     # skip the open paran
    #     index += 1
    #
    #     # Count the un-closed parens as they're encountered
    #     open_parens = 0
    #     # Options in the branching path
    #     options: List[str] = []
    #     current_option = ''
    #
    #     # Found a parenthesis, so split the parenthetical on '|' characters
    #     # (not counting '|' that are nested in more parentheses)
    #     while index < len(path):
    #         if path[index] == ')':
    #             if open_parens > 0:
    #                 # Found a close paren that matches a nested open paren
    #                 open_parens -= 1
    #                 current_option += path[index]
    #             else:
    #                 # Found the close paren that finishes this parenthetical
    #                 options.append(current_option)
    #                 break
    #         elif path[index] == '|' and open_parens == 0:
    #             # Found a pipe that is not nested in a parenthetical
    #             # Add the current option to the list and clear out current_option
    #             options.append(current_option)
    #             current_option = ''
    #         elif path[index] == '(':
    #             # Found an open paren, starting a new nested parenthetical
    #             open_parens += 1
    #             current_option += path[index]
    #         else:
    #             # Found a direction, or a pipe within a nested parenthetical. Add it to the current option
    #             current_option += path[index]
    #         index += 1
    #
    #     # For each option in the parenthetical, start processing from the current room with a new path, built from
    #     # the optional piece of the path, and everything that came after the parenthetical
    #     for opt in options:
    #         self.process_path(current_room.position, opt + path[index+1:])

    def generate_room_distances(self):
        rooms_to_try: Deque[Room] = collections.deque()
        rooms_to_try.append(self.rooms[position_to_key(0, 0)])

        while len(rooms_to_try) > 0:
            room = rooms_to_try.popleft()
            dist = self.dist_to_room[pair_to_key(room.position)]
            for neighbor in room.neighbors.values():
                neighbor_pos = pair_to_key(neighbor.position)
                if neighbor_pos not in self.dist_to_room:
                    self.dist_to_room[neighbor_pos] = dist + 1
                    rooms_to_try.append(neighbor)

    def farthest_room(self):
        return max(self.dist_to_room.values())

    def distant_rooms(self):
        count = 0
        for dist in self.dist_to_room.values():
            if dist >= 1000:
                count += 1
        return count


filename = "test1.txt"
path_input = open(filename).readline()
base = BaseMap(path_input)
base.new_process_path({(0, 0)}, 0)
base.generate_room_distances()
assert (base.farthest_room() == 23)

filename = "test2.txt"
path_input = open(filename).readline()
base = BaseMap(path_input)
base.new_process_path({(0, 0)}, 0)
base.generate_room_distances()
assert (base.farthest_room() == 31)

filename = "input.txt"
path_input = open(filename).readline()
base = BaseMap(path_input)
base.new_process_path({(0, 0)}, 0)
base.generate_room_distances()
print('Part 1: ', base.farthest_room())

print('Part 2: ', base.distant_rooms())