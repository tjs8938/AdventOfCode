from src.Utility.MatrixPrint import *
from src.Utility.Movement2d import *

# filename = "test1.txt"
filename = "input.txt"
grid_input = open(filename).read().splitlines()

mid_y = len(grid_input) // 2
mid_x = len(grid_input[mid_y]) // 2

position = (mid_x, mid_y)
direction = NORTH

grid = {}
for y in range(len(grid_input)):
    for x in range(len(grid_input[y])):
        grid[position_to_key(x, y)] = grid_input[y][x]

turns = {'.': 90, '#': -90, 'F': 180, 'W': 0}
output = {'.': 'W', 'W': '#', '#': 'F', 'F': '.'}

count = 0

for burst in range(10000000):
    key = pair_to_key(position)
    if key not in grid:
        grid[key] = '.'

    value = grid[key]
    direction = turn(direction, turns[value])
    grid[key] = output[value]

    if output[value] == '#':
        count += 1

    position = move(position, direction)

print(count)
