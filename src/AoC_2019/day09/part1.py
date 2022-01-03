import csv

from src.Utility.ThreadedIntCodeComputer import ThreadedIntCodeComputer

file = open('input.txt')

# file = open('test1.txt')  # takes no input and produces a copy of itself as output.
# file = open('test2.txt')  # should output a 16-digit number.
# file = open('test3.txt')  # should output the large number in the middle.


tape = [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')][0]

computer = ThreadedIntCodeComputer(tape.copy())
computer.post_input(2)

computer.start()

computer.join()
print(computer.out_values)
