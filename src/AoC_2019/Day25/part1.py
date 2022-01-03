import csv

from src.Utility.AsciiIntCodeComputer import AsciiIntCodeComputer

file = open('input.txt')
tape = [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')][0]

droid = AsciiIntCodeComputer(tape.copy())

droid.start()

while True:
    stdin = input()
    if stdin == 'exit':
        break
    else:
        droid.accept_str_input(stdin.rstrip())
