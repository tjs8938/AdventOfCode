import csv
from time import sleep

from src.Utility.CyclingOutputThreadedIntCodeComputer import CyclingOutputThreadedIntCodeComputer
from src.Utility.MatrixPrint import position_to_key, dict_to_matrix, print_matrix

file = open('input.txt')

# file = open('test1.txt')  # takes no input and produces a copy of itself as output.
# file = open('test2.txt')  # should output a 16-digit number.
# file = open('test3.txt')  # should output the large number in the middle.


x_pos = 0
y_pos = 0
grid = {}

ball_pos = (0, 0)
paddle_pos = (0, 0)
score = 0

TILES = [' ', 'X', 'B', '_', 'O']


def set_x_pos(x):
    global x_pos
    x_pos = x


def set_y_pos(y):
    global y_pos
    y_pos = y


def add_tile(tile_id):
    global ball_pos, paddle_pos, score
    if x_pos == -1 and y_pos == 0:
        score = tile_id
    else:
        grid[position_to_key(x_pos, y_pos)] = TILES[tile_id]
        if tile_id == 4:
            ball_pos = (x_pos, y_pos)
            direction = 0
            if ball_pos[0] < paddle_pos[0]:
                direction = -1
            elif ball_pos[0] > paddle_pos[0]:
                direction = 1

            computer.post_input(direction)
            matrix = dict_to_matrix(grid, empty=' ')
            print_matrix(matrix)
        elif tile_id == 3:
            paddle_pos = (x_pos, y_pos)


tape = [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')][0]

computer = CyclingOutputThreadedIntCodeComputer(tape.copy())

computer.out_func = [set_x_pos, set_y_pos, add_tile]
computer.start()
computer.join()
print(score)
