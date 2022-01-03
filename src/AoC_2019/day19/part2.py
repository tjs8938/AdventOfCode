import csv
import threading
from datetime import datetime
from math import floor

from src.Utility.MatrixPrint import print_matrix
from src.Utility.ThreadedIntCodeComputer import ThreadedIntCodeComputer

start_time = datetime.now()
EMPTY = '.'
BEAM = '#'

file = open('input.txt')

# file = open('test1.txt')  # takes no input and produces a copy of itself as output.
# file = open('test2.txt')  # should output a 16-digit number.
# file = open('test3.txt')  # should output the large number in the middle.


tape = [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')][0]

computer = None

computer_output = -1
output_mutex = threading.Lock()
output_sem = threading.Semaphore(0)


def half_function():
    print("The thing is done")


def post_location(x, y):
    computer.post_input(x)
    computer.post_input(y)
    output_sem.acquire()
    output_mutex.acquire()
    ret_val = computer_output
    output_mutex.release()
    return ret_val


def receive_output(output):
    global computer_output
    output_mutex.acquire()
    computer_output = output
    output_mutex.release()
    output_sem.release()


def scan(x, y) -> int:
    global computer
    computer = ThreadedIntCodeComputer(tape.copy())
    computer.out_func = receive_output
    computer.start()
    resp = post_location(x, y)
    computer.join()
    return resp


def print_range(x_lo, y_lo, x_hi, y_hi):
    space = []
    row = 0

    for y in range(y_lo, y_hi+1):
        space.append([])
        for x in range(x_lo, x_hi+1):
            resp = scan(x, y)
            space[row].append(BEAM if resp else EMPTY)
        row += 1

    print_matrix(space)


leftest_beam = 0
square_size = 99

x = 0
y = floor(square_size * 1.5)

while True:

    # Find the furthest left beam in this row
    x = leftest_beam
    while scan(x, y) == 0:
        x += 1
    leftest_beam = x

    # Check the spaces at "adjacent corners" of the square
    if scan(x + square_size, y) > 0 and scan(x, y - square_size) > 0 and scan(x + square_size, y - square_size) > 0:
        # found the square!
        # print_range(x-5, y-5-square_size, x+5+square_size, y + 5)
        print(x * 10000 + (y - square_size))
        break

    # Move to the next row
    y += 1


