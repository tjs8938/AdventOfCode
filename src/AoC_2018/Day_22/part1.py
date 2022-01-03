import heapq
from collections import deque
from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import List, Dict, Tuple

# DEPTH = 510
# TARGET = (10, 10)
DEPTH = 4848
TARGET = (15, 700)


class Region(IntEnum):
    ROCKY = 0
    WET = 1
    NARROW = 2


class Tool(Enum):
    NONE = 3
    TORCH = 4
    HOOK = 5


cave_system: Dict[int, Dict[int, int]] = {}
region_types: Dict[int, Dict[int, int]] = {}


def get_geologic_index(x, y) -> int:
    if y not in cave_system or x not in cave_system[y]:

        geologic_index = 0
        if (x, y) not in [(0, 0), TARGET]:
            if y == 0:
                geologic_index = x * 16807
            elif x == 0:
                geologic_index = y * 48271
            else:
                for y_recurse in range(0, y, 200):
                    get_erosion_level(x, y_recurse)
                for x_recurse in range(0, x, 200):
                    get_erosion_level(x_recurse, y)
                geologic_index = get_erosion_level(x - 1, y) * get_erosion_level(x, y - 1)

        if y not in cave_system:
            cave_system[y] = {}
        cave_system[y][x] = geologic_index

    return cave_system[y][x]


def get_erosion_level(x, y) -> int:
    return (get_geologic_index(x, y) + DEPTH) % 20183


def region_type(x, y) -> Region:
    if y not in region_types or x not in region_types[y]:
        t = get_erosion_level(x, y) % 3
        if y not in region_types:
            region_types[y] = {}
        region_types[y][x] = t

    return Region(region_types[y][x])


risk_factor = 0
for y in range(TARGET[1] + 1):
    for x in range(TARGET[0] + 1):
        risk_factor += region_type(x, y)

print("Part 1: ", risk_factor)

# Define the valid options for tool based on region type
TOOL_OPTIONS: Dict[Region, List[Tool]] = {Region.ROCKY: [Tool.HOOK, Tool.TORCH],
                                          Region.WET: [Tool.HOOK, Tool.NONE],
                                          Region.NARROW: [Tool.TORCH, Tool.NONE]}


# Path represents the position of the end of the path, the time it took to get there, and the currently equipped tool
@dataclass
class Path:
    x: int
    y: int
    time: int
    tool: Tool

    def dist_to_target(self):
        return abs(self.x - TARGET[0]) + abs(self.y - TARGET[1])

    def __lt__(self, other):
        return self.time + self.dist_to_target() < other.time + other.dist_to_target()


# index by [y_value][x_value][tool_carried] = best time to this position
best_times: Dict[int, Dict[int, Dict[Tool, int]]] = {}

# The starting paths both start at (0, 0). One starts with the torch (based on instructions) and the other starts with
# the hook and the 7 minutes it takes to switch to the hook
paths = []
first_path = Path(0, 0, 0, Tool.TORCH)
paths.append(first_path)
second_path = Path(0, 0, 7, Tool.HOOK)
paths.append(second_path)


def get_best_time(x, y, tool):
    if y not in best_times:
        best_times[y] = {}
    if x not in best_times[y]:
        best_times[y][x] = {}
    if tool not in best_times[y][x]:
        best_times[y][x][tool] = 2452  # time it took when following a shortest path to the target
    return best_times[y][x][tool]


def set_best_time(x, y, tool, time):
    get_best_time(x, y, tool)
    best_times[y][x][tool] = time


set_best_time(0, 0, Tool.TORCH, 0)
set_best_time(0, 0, Tool.HOOK, 7)

# Breadth first search the possible paths
while len(paths) > 0:

    # get the first path off the queue
    path: Path = heapq.heappop(paths)

    # generate all possible next paths from this one
    for y_offset, x_offset in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        for tool in TOOL_OPTIONS[region_type(path.x, path.y)]:
            new_x = path.x + x_offset
            new_y = path.y + y_offset
            if new_x < 0 or new_y < 0:
                continue

            new_region = region_type(new_x, new_y)

            # only generate the path if the selected tool is valid in the new region
            if tool in TOOL_OPTIONS[new_region]:
                new_time = path.time + 1

                # if the selected tool is not the same as the starting tool, add 7 minutes for the switch
                if tool != path.tool:
                    new_time += 7

                new_path = Path(new_x, new_y, new_time, tool)

                # add empty dictionaries as needed
                if new_y not in best_times:
                    best_times[new_y] = {}
                if new_x not in best_times[new_y]:
                    best_times[new_y][new_x] = {}

                # if the new time is better than the best logged time for this position/tool, log the time and
                # add the path to the queue for BFS. Also check the target position with torch, as that is
                # the end condition
                if new_time < get_best_time(new_x, new_y, tool) and \
                        new_time + new_path.dist_to_target() < get_best_time(TARGET[0], TARGET[1], Tool.TORCH):
                    best_times[new_y][new_x][tool] = new_time
                    heapq.heappush(paths, new_path)

print("Part 2: ", get_best_time(TARGET[0], TARGET[1], Tool.TORCH))
