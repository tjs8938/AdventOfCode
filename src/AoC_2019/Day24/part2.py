from collections import deque
from dataclasses import dataclass
from typing import List


@dataclass
class Bitmask:
    bitmask: int
    lower_bitmask: int = 0
    upper_bitmask: int = 0

    def __lshift__(self, other):
        return self.bitmask << other

    def __int__(self):
        return self.bitmask

    def upper_level(self, *args):
        for a in args:
            self.upper_bitmask += pow(2, a)

    def lower_level(self, *args):
        for a in args:
            self.lower_bitmask += pow(2, a)


def build_bitmask(*args) -> int:
    value = 0
    for a in args:
        value += pow(2, a)
    return value


TOP_LEFT = build_bitmask(1, 5)
TOP = build_bitmask(0, 2, 6)
TOP_RIGHT = build_bitmask(3, 9)
LEFT = build_bitmask(0, 6, 10)
INSIDE = build_bitmask(1, 5, 7, 11)
RIGHT = build_bitmask(4, 8, 14)
BOTTOM_LEFT = build_bitmask(15, 21)
BOTTOM = build_bitmask(20, 16, 22)
BOTTOM_RIGHT = build_bitmask(23, 19)
BITMASK_INTS: List[int] = [TOP_LEFT, TOP, TOP << 1, TOP << 2, TOP_RIGHT,
                           LEFT, INSIDE, INSIDE << 1, INSIDE << 2, RIGHT,
                           LEFT << 5, INSIDE << 5, 0, INSIDE << 7, RIGHT << 5,
                           LEFT << 10, INSIDE << 10, INSIDE << 11, INSIDE << 12, RIGHT << 10,
                           BOTTOM_LEFT, BOTTOM, BOTTOM << 1, BOTTOM << 2, BOTTOM_RIGHT
                           ]

BITMASKS: List[Bitmask] = [Bitmask(i) for i in BITMASK_INTS]

BITMASKS[11].lower_level(0, 5, 10, 15, 20)
BITMASKS[13].lower_level(4, 9, 14, 19, 24)
BITMASKS[7].lower_level(0, 1, 2, 3, 4)
BITMASKS[17].lower_level(20, 21, 22, 23, 24)

for i in range(0, 5):
    BITMASKS[i].upper_level(7)

for i in range(20, 25):
    BITMASKS[i].upper_level(17)

for i in range(4, 25, 5):
    BITMASKS[i].upper_level(13)

for i in range(0, 21, 5):
    BITMASKS[i].upper_level(11)


def count_enabled_bits(*args) -> int:
    count = 0
    for val in args:
        while val > 0:
            val = val & (val - 1)
            count += 1
    return count


def get_next_bio_value(biodiversity_rating, lower, upper):
    next_bio_rating = biodiversity_rating
    index_mask = 1
    for index in range(0, 25):
        surrounding_spaces = biodiversity_rating & BITMASKS[index].bitmask
        surrounding_spaces_low = lower & BITMASKS[index].lower_bitmask
        surrounding_spaces_up = upper & BITMASKS[index].upper_bitmask
        bit_count = count_enabled_bits(surrounding_spaces, surrounding_spaces_up, surrounding_spaces_low)
        if biodiversity_rating & index_mask > 0:
            # This space has a bug
            if bit_count != 1:
                # the number of neighbors is not exactly 1, so kill the bug
                next_bio_rating ^= index_mask
        else:
            # this space is empty
            if bit_count in [1, 2]:
                # infest this space
                next_bio_rating ^= index_mask
        index_mask <<= 1

    return next_bio_rating


def part2(filename: str, time: int) -> int:
    input_chars = "".join(open(filename).read().splitlines())
    pow = 1
    biodiversity_rating = 0
    for c in input_chars:
        if c == '#':
            biodiversity_rating += pow
        pow <<= 1

    levels = deque()
    levels.append(0)
    levels.append(biodiversity_rating)
    levels.append(0)

    for t in range(0, time):
        if levels[1] > 0:
            levels.appendleft(0)
        if levels[-2] > 0:
            levels.append(0)

        new_levels = deque()
        new_levels.append(0)
        for l in range(1, len(levels) - 1):
            lower = levels[l-1]
            current = levels[l]
            upper = levels[l+1]
            new_rating = get_next_bio_value(current, lower, upper)
            new_levels.append(new_rating)

        new_levels.append(0)
        levels = new_levels

    total_bugs = count_enabled_bits(*levels)
    return total_bugs


print(part2("test1.txt", 10))
print(part2("input.txt", 200))
