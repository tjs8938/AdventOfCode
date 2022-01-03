import itertools
import math
import re

from src.aoc_frame import run_part


def part_a(input_data: str) -> str:
    pattern = re.compile('target area: x=([0-9]*)..([0-9]*), y=(-[0-9]*)..(-[0-9]*)')
    m = pattern.match(input_data)
    x_range = (int(m.group(1)), int(m.group(2)))
    y_range = (int(m.group(4)), int(m.group(3)))
    # print(x_range, y_range)

    x_v = math.ceil(math.sqrt(2 * x_range[0] + .25) - .5)
    #
    # best_y = 0
    # y = 0
    # while True:
    #     step = 0
    #     current_y = 0
    #     while current_y > y_range[0]:
    #         current_y -= (y + step)
    #         step += 1
    #     if current_y - (y + step) >= y_range[1]:
    #         best_y = y
    #     elif best_y > 0:
    #         break
    #     y += 1
    #
    # print(best_y)

    best_y_vel = -1 * y_range[1] - 1
    best_height = (best_y_vel * (best_y_vel + 1)) // 2

    return str(int(best_height))


def sim_vel(x_v, y_v, x_range, y_range) -> bool:
    initial_x = x_v
    x_pos = 0
    y_pos = 0

    # quickly adjust for positive y velocity
    # if y_v > 0:
    #     steps = 2*y_v
    #     y_v = -1 - y_v
    #
    #     if x_v <= steps:
    #         x_pos = int(x_v * (x_v + 1) // 2)
    #         x_v = 0
    #     else:
    #         x_pos = int(steps * (2 * x_v - steps + 1) // 2)
    #         x_v -= (steps + 1)

    while True:
        if x_range[0] <= x_pos <= x_range[1] and y_range[0] >= y_pos >= y_range[1]:
            return True
        elif x_pos > x_range[1] or y_pos < y_range[1]:
            return False
        x_pos += x_v
        y_pos += y_v
        y_v -= 1
        x_v = 0 if x_v == 0 else x_v - 1


def part_b(input_data: str) -> str:

    pattern = re.compile('target area: x=([0-9]*)..([0-9]*), y=(-[0-9]*)..(-[0-9]*)')
    m = pattern.match(input_data)
    x_range = (int(m.group(1)), int(m.group(2)))
    y_range = (int(m.group(4)), int(m.group(3)))

    max_y_vel = -1 * y_range[1] - 1
    min_y_vel = y_range[1]

    min_x_vel = 0 # math.ceil(math.sqrt(2 * x_range[0] + .25) - .5)
    max_x_vel = x_range[1]

    count = 0

    for x_v, y_v in itertools.product(range(min_x_vel, max_x_vel + 1), range(min_y_vel, max_y_vel + 1)):
        if sim_vel(x_v, y_v, x_range, y_range):
            count += 1

    print((min_x_vel, max_x_vel), (min_y_vel, max_y_vel))

    return str(count)


# run_part(part_a, 'a', 2021, 17)
run_part(part_b, 'b', 2021, 17)

