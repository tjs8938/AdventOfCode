import copy
import heapq
from dataclasses import dataclass
from typing import List, Set

from aocd.transforms import lines

from src.aoc_frame import run_part


def parse_input(input_data: str) -> List[str]:
    in_lines = lines(input_data)
    first_pos = [in_lines[2][i * 2 + 3] for i in range(4)]
    second_pos = [in_lines[3][i * 2 + 3] for i in range(4)]
    return [a + b for a, b in zip(first_pos, second_pos)]


def part_a(input_data: str) -> str:
    rooms = parse_input(input_data)
    print(rooms)
    return solve(rooms)


def part_b(input_data: str) -> str:
    rooms = parse_input(input_data)
    inserts = ['DD', 'CB', 'BA', 'AC']
    for i in range(4):
        rooms[i] = rooms[i][0] + inserts[i] + rooms[i][1]
    print(rooms)
    return solve(rooms)


@dataclass
class State:
    rooms: List[str]
    hall: str = '...........'
    cost: int = 0

    def __lt__(self, other):
        return self.cost < other.cost

    def __hash__(self):
        return hash((self.cost, self.hall, self.rooms[0], self.rooms[1], self.rooms[2], self.rooms[3]))


def l_to_idx(letter: str) -> int:
    return ord(letter) - ord('A')


def solve(in_rooms: List[str]) -> str:
    start_state = State(in_rooms)
    paths = [start_state]
    room_size = len(in_rooms[0])
    states_seen: Set = {start_state}

    stop_condition = ['A' * room_size, 'B' * room_size, 'C' * room_size, 'D' * room_size]

    states_examined = 0
    while len(paths) > 0:
        path = heapq.heappop(paths)
        if path.rooms == stop_condition:
            print(states_examined)
            return str(path.cost)
        states_examined += 1

        # Check all amphipods in the hallway
        for hall_idx in range(len(path.hall)):
            cur_l = path.hall[hall_idx]
            if cur_l == '.':
                continue

            room = path.rooms[l_to_idx(cur_l)]
            if len(room) == room.count(cur_l):
                # The room is open
                room_hall_idx = l_to_idx(cur_l) * 2 + 2
                hall_path = path.hall[room_hall_idx:hall_idx] if room_hall_idx < hall_idx \
                    else path.hall[hall_idx + 1: room_hall_idx + 1]
                if len(hall_path) == hall_path.count('.'):
                    # the hall is clear
                    move_length = len(hall_path) + room_size - len(room)
                    move_cost = move_length * pow(10, l_to_idx(cur_l))

                    new_state = copy.deepcopy(path)
                    new_state.hall = new_state.hall[:hall_idx] + '.' + new_state.hall[hall_idx + 1:]
                    new_state.rooms[l_to_idx(cur_l)] += cur_l
                    new_state.cost += move_cost

                    if new_state.rooms == stop_condition:
                        print(states_examined)
                        return str(new_state.cost)
                    elif new_state not in states_seen:
                        states_seen.add(new_state)
                        heapq.heappush(paths, new_state)

        # Check the amphipods in the rooms
        for room_idx in range(4):
            room = path.rooms[room_idx]
            if len(room) == 0:
                # Empty room, nothing to do
                continue

            cur_l = room[0]
            room_hall_idx = room_idx * 2 + 2
            if l_to_idx(cur_l) == room_idx and len(room) == room.count(cur_l):
                # all amphipods in this room are in the right room
                continue

            # Move the first amphipod into the hall
            hall_options = [0, 1, 3, 5, 7, 9, 10]  # Skip the positions directly outside a room
            for hall_idx in hall_options:
                if path.hall[hall_idx] != '.':
                    # This position is occupied in the hall
                    continue

                hall_l, hall_r = (room_hall_idx, hall_idx) if room_hall_idx < hall_idx else (hall_idx, room_hall_idx)
                hall_path = path.hall[hall_l:hall_r + 1]

                # the hall is clear
                if len(hall_path) == hall_path.count('.'):

                    move_length = len(hall_path) + room_size - len(room)
                    move_cost = move_length * pow(10, l_to_idx(cur_l))

                    new_state = copy.deepcopy(path)
                    new_state.hall = new_state.hall[:hall_idx] + cur_l + new_state.hall[hall_idx + 1:]
                    new_state.rooms[room_idx] = new_state.rooms[room_idx][1:]
                    new_state.cost += move_cost

                    if new_state not in states_seen:
                        states_seen.add(new_state)
                        heapq.heappush(paths, new_state)

    return '0'


# run_part(part_a, 'a', 2021, 23)
run_part(part_b, 'b', 2021, 23)
