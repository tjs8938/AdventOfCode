import csv
import itertools

from src.day07.IntCodeComputer import IntCodeComputer

file = open('input.txt')

# file = open('test1.txt')  # Max thruster signal 43210 (from phase setting sequence 4,3,2,1,0)
# file = open('test2.txt')  # Max thruster signal 54321 (from phase setting sequence 0,1,2,3,4)
# file = open('test3.txt')  # Max thruster signal 65210 (from phase setting sequence 1,0,4,3,2)


tape = [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')][0]

phase_settings = itertools.permutations(['0', '1', '2', '3', '4'])

max_output = 0
max_phase_settings = None

for test_phases in phase_settings:
    previous_output = 0
    for phase in test_phases:
        in_params = [int(phase), previous_output]
        comp = IntCodeComputer(tape.copy(), in_params)
        comp.run()
        previous_output = comp.out_values[0]

    if previous_output > max_output:
        max_output = previous_output
        max_phase_settings = test_phases

print(max_phase_settings, max_output)
