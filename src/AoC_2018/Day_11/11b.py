from itertools import permutations
from pprint import pprint

serial = 8561
GRID_SIZE = 300

def calcPower(x, y):
    rackId = x + 10
    power = (rackId * y + serial) * rackId
    power = int((power % 1000) / 100)
    return power - 5


cells = [[calcPower(x, y) for x in range(1, GRID_SIZE+1)] for y in range(1, GRID_SIZE+1)]

max_x = 0
max_y = 0
max_value = -1000000000
max_square = 0
summed_area = []
for y in range(1, GRID_SIZE+1):
    summed_area.append([])
    for x in range(1, GRID_SIZE+1):
        power = cells[y-1][x-1]
        if x > 1:
            power += summed_area[y-1][x-2]

        if y > 1:
            power += summed_area[y-2][x-1]

        if x > 1 and y > 1:
            power -= summed_area[y-2][x-2]

        summed_area[y - 1].append(power)

# pprint(cells)
for square in range(1, GRID_SIZE+1):
    for y in range(square, GRID_SIZE+1):
        for x in range(square, GRID_SIZE+1):
            area_sum = summed_area[y-1][x-1]
            if y > square:
                area_sum -= summed_area[y-square-1][x-1]

            if x > square:
                area_sum -= summed_area[y-1][x-square-1]

            if y > square and x > square:
                area_sum += summed_area[y-square-1][x-square-1]

            if max_value < area_sum:
                max_value = area_sum
                max_x = x
                max_y = y
                max_square = square

# pprint(summed_area)
# pprint(cells)

print(max_x-max_square+1, max_y-max_square+1, max_square, max_value)
