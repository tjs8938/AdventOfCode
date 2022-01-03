import csv
import threading

from src.Utility import MatrixPrint
from src.Utility.MatrixPrint import pair_to_key
from src.Utility.ThreadedIntCodeComputer import ThreadedIntCodeComputer

file = open('input.txt')

# file = open('test1.txt')  # takes no input and produces a copy of itself as output.
# file = open('test2.txt')  # should output a 16-digit number.
# file = open('test3.txt')  # should output the large number in the middle.


tape = [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')][0]

droid = ThreadedIntCodeComputer(tape.copy())

droid_output = -1
output_mutex = threading.Lock()
output_sem = threading.Semaphore(0)


def post_direction(direction):
    droid.post_input(direction)
    output_sem.acquire()
    output_mutex.acquire()
    ret_val = droid_output
    output_mutex.release()
    return ret_val


def receive_output(output):
    global droid_output
    output_mutex.acquire()
    droid_output = output
    output_mutex.release()
    output_sem.release()


NORTH = 0
WEST = 1
SOUTH = 2
EAST = 3

WALL = '#'
OXYGEN = 'O'
EMPTY = '.'

droid_pos = (0, 0)
oxygen_pos = None
ship_map = {pair_to_key(droid_pos): 'X'}
move_count = 0

MOVEMENTS = [
    1,
    3,
    2,
    4
]

MOVE = [
    lambda x: (x[0], x[1] - 1),
    lambda x: (x[0] - 1, x[1]),
    lambda x: (x[0], x[1] + 1),
    lambda x: (x[0] + 1, x[1])
]


def about_face(direction):
    return direction ^ 2


def try_movement(direction) -> bool:
    global ship_map, droid_pos, oxygen_pos
    result = post_direction(MOVEMENTS[direction])
    space_ahead = MOVE[direction](droid_pos)

    if result == 0:
        ship_map[pair_to_key(space_ahead)] = WALL
        return False
    elif ship_map.get(pair_to_key(space_ahead)) is None:
        if result == 2:
            ship_map[pair_to_key(space_ahead)] = OXYGEN
            oxygen_pos = space_ahead
            print(move_count+1)
        else:
            ship_map[pair_to_key(space_ahead)] = EMPTY

    droid_pos = space_ahead
    return True


def look_dir(direction):
    next_space = pair_to_key(MOVE[direction](droid_pos))
    return ship_map.get(next_space, None)


def move(direction):
    global move_count
    if look_dir(direction) is not None:
        return

    if not try_movement(direction):
        return

    move_count += 1
    for dir in range(0, 4):
        move(dir)

    try_movement(about_face(direction))
    move_count -= 1


droid.out_func = receive_output
droid.start()

for dir in range(0, 4):
    move(dir)

map_grid = MatrixPrint.dict_to_matrix(ship_map)
MatrixPrint.print_matrix(map_grid)

print(oxygen_pos)
droid.join()
