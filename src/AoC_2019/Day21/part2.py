import csv

from src.Utility.AsciiIntCodeComputer import AsciiIntCodeComputer

file = open('input.txt')

tape = [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')][0]

computer = AsciiIntCodeComputer(tape.copy())

computer.accept_str_input("NOT A T")
computer.accept_str_input("NOT B J")
computer.accept_str_input("OR T J")
computer.accept_str_input("NOT C T")
computer.accept_str_input("OR T J")
computer.accept_str_input("AND D J")
computer.accept_str_input("NOT E T")
computer.accept_str_input("NOT T T")
computer.accept_str_input("OR H T")
computer.accept_str_input("AND T J")
computer.accept_str_input("RUN")

computer.start()
computer.join()

print(computer.out_values[-1])