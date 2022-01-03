import csv
import threading
from datetime import datetime

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


space = []

for y in range(0, 50):
    space.append([])
    for x in range(0, 50):
        resp = scan(x, y)
        space[y].append(BEAM if resp else EMPTY)

print_matrix(space)

flat_list = [item for sublist in space for item in sublist]
print(len(list(filter(lambda x: x == BEAM, flat_list))))
print(datetime.now() - start_time)
