import csv
import itertools

from src.day07.ThreadedIntCodeComputer import ThreadedIntCodeComputer

file = open('input.txt')

# file = open('test4.txt')  # Max thruster signal 139629729 (from phase setting sequence 9,8,7,6,5)
# file = open('test5.txt')  # Max thruster signal 18216 (from phase setting sequence 9,7,8,5,6)


tape = [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')][0]

phase_settings = itertools.permutations(['5', '6', '7', '8', '9'])
# phase_settings = [['5', '6', '7', '8', '9']]

max_output = 0
max_phase_settings = None

for test_phases in phase_settings:

    computers = [ThreadedIntCodeComputer(tape.copy(), int(phase)) for phase in test_phases]

    for i in range(0, len(computers)):
        computers[i].out_func = computers[(i+1) % len(computers)].post_input
        if i == 0:
            computers[i].post_input(0)
        computers[i].start()

    for comp in computers:
        comp.join()

    previous_output = computers[-1].out_values[-1]
    if previous_output > max_output:
        max_output = previous_output
        max_phase_settings = test_phases

print(max_phase_settings, max_output)
