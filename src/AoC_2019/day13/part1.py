import csv

from src.Utility.CyclingOutputThreadedIntCodeComputer import CyclingOutputThreadedIntCodeComputer
from src.Utility.MatrixPrint import position_to_key

file = open('input.txt')

# file = open('test1.txt')  # takes no input and produces a copy of itself as output.
# file = open('test2.txt')  # should output a 16-digit number.
# file = open('test3.txt')  # should output the large number in the middle.


x_pos = 0
y_pos = 0
grid = {}


def set_x_pos(x):
    global x_pos
    x_pos = x


def set_y_pos(y):
    global y_pos
    y_pos = y


def add_tile(tile_id):
    grid[position_to_key(x_pos, y_pos)] = tile_id


tape = [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')][0]

computer = CyclingOutputThreadedIntCodeComputer(tape.copy())

computer.out_func = [set_x_pos, set_y_pos, add_tile]
computer.start()

computer.join()
print(len(list(filter(lambda x: x == 2, grid.values()))))

