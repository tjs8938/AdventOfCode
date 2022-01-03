import csv

from src.Utility.AsciiIntCodeComputer import AsciiIntCodeComputer
from src.Utility.MatrixPrint import print_matrix

file = open('input')

# file = open('test1.txt')  # takes no input and produces a copy of itself as output.
# file = open('test2.txt')  # should output a 16-digit number.
# file = open('test3.txt')  # should output the large number in the middle.

SCAFFOLD = '#'
SPACE = '.'

tape = [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')][0]

computer = AsciiIntCodeComputer(tape.copy())

computer.start()
computer.join()

scaffold = list(filter(lambda x: x != "", computer.output_strings))
alignment_sum = 0

for y in range(1, len(scaffold) - 1):
    for x in range(1, len(scaffold[y]) - 1):
        if SPACE not in (scaffold[y][x], scaffold[y][x-1], scaffold[y][x+1], scaffold[y-1][x], scaffold[y+1][x]):
            alignment_sum += x*y

print(alignment_sum)
