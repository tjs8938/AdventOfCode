import csv

from src.Utility.ThreadedIntCodeComputer import ThreadedIntCodeComputer

file = open('input.txt')

# file = open('test1.txt')  # takes no input and produces a copy of itself as output.
# file = open('test2.txt')  # should output a 16-digit number.
# file = open('test3.txt')  # should output the large number in the middle.


tape = [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')][0]

robot = ThreadedIntCodeComputer(tape.copy())

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

MOVE = [lambda x: (x[0], x[1] - 1),
        lambda x: (x[0] + 1, x[1]),
        lambda x: (x[0], x[1] + 1),
        lambda x: (x[0] - 1, x[1])
        ]

TURN = [lambda x: x - 1,
        lambda x: x + 1]

position = (0, 0)
panels = {}
direction = UP
action_count = 0

debug = False


def position_to_key(x):
    return str(x[0]) + ',' + str(x[1])


def paint_panel(color):
    panels[position_to_key(position)] = color
    if debug:
        print("Painting " + ("black" if color == 0 else "white"))


def scan_panel():
    color = panels.get(position_to_key(position), 0)
    robot.post_input(color)
    if debug:
        print("Scanning " + ("black" if color == 0 else "white"))


def turn(rotation):
    global direction
    direction = TURN[rotation](direction) % 4
    if debug:
        print("Turning " + ("counter-clockwise" if rotation == 0 else "clockwise"))


def move():
    global position
    position = MOVE[direction](position)
    if debug:
        print("Moving to position " + str(position))


def action(value):
    global action_count

    if action_count % 2 == 0:
        paint_panel(value)
    else:
        turn(value)
        move()
        scan_panel()

    action_count += 1


robot.post_input(1)
robot.out_func = action
robot.start()
robot.join()

print(len(panels.values()))



# 7139 too high
