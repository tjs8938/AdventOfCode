import csv

from src.Utility.AsciiIntCodeComputer import AsciiIntCodeComputer

file = open('input')

# file = open('test1.txt')  # takes no input and produces a copy of itself as output.
# file = open('test2.txt')  # should output a 16-digit number.
# file = open('test3.txt')  # should output the large number in the middle.

SCAFFOLD = '#'
SPACE = '.'

tape = [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')][0]

# Force the vacuum robot to wake up by changing the value in your ASCII program at address 0 from 1 to 2.
tape[0] = 2
computer = AsciiIntCodeComputer(tape.copy())


# Potential Path
# R,10,R,8,L,10,L,10,R,8,L,6,L,6,R,8,L,6,L,6,R,10,R,8,L,10,L,10,L,10,R,10,L,6,R,8,L,6,L,6,L,10,R,10,L,6,L,10,R,10,L,6,R,8,L,6,L,6,R,10,R,8,L,10,L,10
# A,B,B,A,C,B,C,C,B,A
# A = R,10,R,8,L,10,L,10
# B = R,8,L,6,L,6
# C = L,10,R,10,L,6

# Post main movement routine
computer.accept_str_input("A,B,B,A,C,B,C,C,B,A")

# Post movement functions

computer.accept_str_input("R,10,R,8,L,10,L,10")
computer.accept_str_input("R,8,L,6,L,6")
computer.accept_str_input("L,10,R,10,L,6")

# Finally, you will be asked whether you want to see a continuous video feed; provide either y or n and a newline
computer.accept_str_input('n')

computer.start()
computer.join()

print(computer.out_values[-1])
