from __future__ import annotations
import re
from dataclasses import dataclass

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


bots = []
filename = "input.txt"
for line in open(filename).read().splitlines():
    m = pattern.match(line)
    bot = Bot(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)))
    bots.append(bot)

bots.sort(reverse=True)


biggest_radius = bots[0]
bots_in_range = list(filter(lambda b: biggest_radius.in_range(b), bots))

print("Part 1: ", len(bots_in_range))

