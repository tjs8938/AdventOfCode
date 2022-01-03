import re
from typing import Tuple, List

pattern = re.compile("(\\d*)-(\\d*)")

input_lines = open("input.txt").read().splitlines()


blocked_list: List[Tuple[int, int]] = []
for line in input_lines:
    m = pattern.match(line)
    blocked_list.append((int(m.group(1)), int(m.group(2))))

blocked_list.sort(key=lambda x: x[0])

best_available = 0
for block in blocked_list:
    if block[0] <= best_available <= block[1]:
        best_available = block[1] + 1
    elif block[0] > best_available:
        print(best_available)
        exit(0)