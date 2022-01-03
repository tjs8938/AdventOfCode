from itertools import permutations
from pprint import pprint

serial = 8561


def calcPower(x, y):
    rackId = x + 10
    power = (rackId * y + serial) * rackId
    power = int((power % 1000) / 100)
    return power - 5


max_x = 0
max_y = 0
max_value = 0
cells = []
for y in range(1, 301):
    cells.append([])
    for x in range(1, 301):
        cells[y - 1].append(0)
        power = calcPower(x, y)
        for i in range(1, 4):
            for j in range(1, 4):
                if x - i >= 0 and y - j >= 0:
                    cells[y - j][x - i] += power

for y in range(len(cells)):
    for x in range(len(cells[y])):
        if max_value < cells[y][x]:
            max_value = cells[y][x]
            max_x = x
            max_y = y

# pprint(cells)

print(max_x + 1, max_y + 1, max_value)
