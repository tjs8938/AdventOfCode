from __future__ import annotations

import heapq
import math
import re
from collections import deque
from copy import copy
from dataclasses import dataclass
from datetime import datetime
from typing import Tuple, Set

pattern = re.compile("pos=<(.*),(.*),(.*)>, r=(.*)")


@dataclass
class Bot:
    x: int
    y: int
    z: int
    r: int

    def __lt__(self, other: Bot):
        return self.r < other.r

    def in_range(self, other: Bot):
        dist = abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)
        return dist <= self.r

    def point_in_range(self, point: Tuple[int, int, int]):
        dist = abs(self.x - point[0]) + abs(self.y - point[1]) + abs(self.z - point[2])
        return dist <= self.r

    def __hash__(self):
        return hash(self.__repr__())


bots = []
# filename = "test2.txt"
filename = "input.txt"
for line in open(filename).read().splitlines():
    m = pattern.match(line)
    bot = Bot(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)))
    bots.append(bot)

bots.sort(reverse=True)

biggest_radius = bots[0]
bots_in_range = list(filter(lambda b: biggest_radius.in_range(b), bots))

print("Part 1: ", len(bots_in_range))

# Find min value among the bots for each dimension
#    Center - radius
start_time = datetime.now()
min_x = min(bot.x - bot.r for bot in bots)
min_y = min(bot.y - bot.r for bot in bots)
min_z = min(bot.z - bot.r for bot in bots)

# Shift each bot by the min value so that all points within any bot range is all positive values
for bot in bots:
    bot.x -= min_x
    bot.y -= min_y
    bot.z -= min_z

# Find maximum value in any direction, including radius
global_max = max(max(bot.x, bot.y, bot.z) for bot in bots)

# Find smallest power of 2 that is greater (or equal to) than the above maximum.
# This is the side length of the starting cube
initial_cube_size = pow(2, math.ceil(math.log2(global_max)))


# A cube is defined by the location of its corner which is closest to the origin, and it’s side length
class Cube:

    def __init__(self, position: Tuple[int, int, int], side: int):

        self.position = position
        self.side = side
        self.bots_in_range: Set[Bot] = set()
        self.bot_intersecting: Set[Bot] = set()

    def __hash__(self):
        return hash((self.position, self.side))

    def __eq__(self, other):
        return self.position == other.position and self.side == other.side

    def __lt__(self, other: Cube):
        if len(self.bots_in_range) + len(self.bot_intersecting) > len(other.bots_in_range) + len(other.bot_intersecting):
            return True
        if len(other.bots_in_range) + len(other.bot_intersecting) > len(self.bots_in_range) + len(self.bot_intersecting):
            return False

        if self.side > other.side:
            return True
        if other.side > self.side:
            return False

        if self.position[0] + self.position[1] + self.position[2] < \
                other.position[0] + other.position[1] + other.position[2]:
            return True
        return False

    def completely_in_range(self, bot: Bot) -> bool:
        all_in_range = True
        for corner in self.get_corners(self.side):
            if not bot.point_in_range(corner):
                all_in_range = False
                break
        return all_in_range

    def does_intersect(self, bot: Bot) -> bool:

        # Next check if any point in the cube can be reached by the bot
        dist = 0
        dist += abs(bot.x - self.position[0]) + abs(bot.x - (self.position[0] + self.side)) - self.side
        dist += abs(bot.y - self.position[1]) + abs(bot.y - (self.position[1] + self.side)) - self.side
        dist += abs(bot.z - self.position[2]) + abs(bot.z - (self.position[2] + self.side)) - self.side
        dist //= 2

        # If the distance to the nearest edge of the cube is within the radius, there is an intersection
        return dist <= bot.r

    def split_cube(self) -> Set[Cube]:
        new_side = self.side // 2

        # special case for a side of 0, where the new points should still be 1 unit away
        if new_side > 0:
            shift = new_side
        else:
            shift = 1

        split_cubes = set()
        for corner in self.get_corners(shift):
            smaller_cube = Cube(corner, new_side)
            smaller_cube.bots_in_range = copy(self.bots_in_range)
            for intersecting_bot in self.bot_intersecting:
                if smaller_cube.completely_in_range(intersecting_bot):
                    smaller_cube.bots_in_range.add(intersecting_bot)
                elif smaller_cube.does_intersect(intersecting_bot):
                    smaller_cube.bot_intersecting.add(intersecting_bot)
            split_cubes.add(smaller_cube)

        return split_cubes

    def get_corners(self, shift) -> Set[Tuple[int, int, int]]:
        corners = set()
        for i in range(8):
            new_pos = (self.position[0] + (shift * (i & 1)),
                       self.position[1] + (shift * ((i & 2) >> 1)),
                       self.position[2] + (shift * ((i & 4) >> 2)))
            corners.add(new_pos)
        return corners


# Create a queue of cubes to analyze, and place the starting box in the queue
cube_queue = []

first_cube = Cube((0, 0, 0), initial_cube_size)
first_cube.bot_intersecting = copy(bots)
cube_queue.append(first_cube)

highest_bot_count = 500

# Create an empty set of cubes that do not intersect any sphere
completed_cubes: Set[Cube] = set()

# While there are cubes in the queue:
while len(cube_queue) > 0:
    # Pop a cube off the queue
    current_cube: Cube = heapq.heappop(cube_queue)
    if len(current_cube.bots_in_range) + len(current_cube.bot_intersecting) >= highest_bot_count:
        split_cubes = current_cube.split_cube()

        for small_cube in split_cubes:
            if len(small_cube.bot_intersecting) == 0:
                completed_cubes.add(small_cube)
            elif len(small_cube.bots_in_range) + len(small_cube.bot_intersecting) >= highest_bot_count:
                if len(small_cube.bots_in_range) >= highest_bot_count:
                    highest_bot_count = len(small_cube.bots_in_range)
                heapq.heappush(cube_queue, small_cube)

# For each cube in the set, determine how many spheres include the corner
# Keep only the cubes that tie for the largest number of spheres
best_count = 0
best_cubes = set()
for c in completed_cubes:
    spheres = sum(1 if bot.point_in_range(c.position) else 0 for bot in bots)
    if spheres > best_count:
        best_count = spheres
        best_cubes = set()
        best_cubes.add(c)
    elif spheres == best_count:
        best_cubes.add(c)

# Add all 8 corners from each cube to a set of points to analyze, shifting each back by the offsets from earlier
best_corners = set()
for c in best_cubes:
    for point in c.get_corners(c.side):
        shifted_point = (point[0] + min_x, point[1] + min_y, point[2] + min_z)
        best_corners.add(shifted_point)

# For each point in the set, determine which is closest to the origin. This Manhattan distance is the answer to part 2
man_dist = min(abs(p[0]) + abs(p[1]) + abs(p[2]) for p in best_corners)

print("Part 2: ", man_dist)
print(datetime.now() - start_time)