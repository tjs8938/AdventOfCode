import re
from typing import List, Dict

from src.AoC_2017.Day12.House import House


def get_house(houses: Dict[str, House], house_num: str) -> House:
    if house_num not in houses:
        houses[house_num] = House(house_num)
    return houses[house_num]


def reachable_from_0(filename: str) -> int:
    neighborhood = open(filename).read().splitlines()

    # build all houses
    houses: Dict[str, House] = {}
    for line in neighborhood:
        m = re.match('([0-9]+) <-> (.*)', line)
        house = get_house(houses, m.group(1))
        house.neighbors = set(map(lambda house_num: get_house(houses, house_num), m.group(2).split(', ')))

    # map the distances between houses
    nodes_to_process: List[House] = list(houses.values())
    while len(nodes_to_process) > 0:
        process = nodes_to_process.pop(0)
        for neighbor in process.neighbors:
            changed = False
            for loc, dist in process.dist_to_loc.items():
                if loc not in neighbor.dist_to_loc or neighbor.dist_to_loc[loc] > dist + 1:
                    neighbor.dist_to_loc[loc] = dist + 1
                    changed = True

            if changed:
                nodes_to_process.append(neighbor)

    return len(houses['0'].dist_to_loc)


assert(reachable_from_0("test1.txt") == 6)
print(reachable_from_0("input.txt"))
