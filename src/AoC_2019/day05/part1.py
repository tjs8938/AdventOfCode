import csv
import math

file = open('input.txt')
tape = [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')][0]

param_counts = [0, 3, 3, 1, 1]
pc = 0


def add(modes):
    addend1 = get_param(True, modes[0])
    addend2 = get_param(True, modes[1])
    tape[get_param(False, modes[2])] = addend1 + addend2


def multiply(modes):
    factor1 = get_param(True, modes[0])
    factor2 = get_param(True, modes[1])
    tape[get_param(False, modes[2])] = factor1 * factor2


def parse_instruction():
    global pc
    instruction = tape[pc]
    opcode = instruction % 100  # grab the last 2 digits of the pc as the opcode
    param_count = param_counts[opcode]
    # print(tape[pc:pc+param_count+1])

    pc += 1

    modes = []
    if opcode != 99:
        # The hundreds digit is the parameter mode for the first parameter, and each digit above that is used as the
        # parameter mode for successive parameters
        divisor = 100
        for p_count in range(0, param_count):
            modes.append(math.floor(instruction / divisor) % 10)
            divisor *= 10

    return opcode, modes


def get_param(input_param, mode):
    global pc
    pc += 1
    if mode == 0 and input_param:
        return tape[tape[pc-1]]
    else:
        return tape[pc-1]


def input(modes):
    tape[get_param(False, modes[0])] = 1


def output(modes):
    print(get_param(True, modes[0]))


while tape[pc] != 99:
    opcode, parameters = parse_instruction()
    if opcode == 1:
        add(parameters)
    elif opcode == 2:
        multiply(parameters)
    elif opcode == 3:
        input(parameters)
    elif opcode == 4:
        output(parameters)
    else:
        break
