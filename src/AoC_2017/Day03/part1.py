import math


def count_steps(x: int) -> int:
    ring = math.floor((math.sqrt(x - 1) + 1) / 2)
    corner = math.pow((2 * ring) - 1, 2)
    steps = int(ring + abs(((x-corner) % (2 * ring)) - ring))
    return steps


assert(count_steps(26) == 5)
# assert(count_steps(1) == 0)
assert(count_steps(12) == 3)
assert(count_steps(23) == 2)
assert(count_steps(1024) == 31)
print(count_steps(347991))
