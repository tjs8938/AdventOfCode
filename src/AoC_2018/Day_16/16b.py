#!/bin/python
import re
from pprint import pprint

file = open("input1", 'r')

regex = re.compile('([0-9]+)')


def addr(a, b, c):
    result = registers.copy()
    result[c] = result[a] + result[b]
    return result


def addi(a, b, c):
    result = registers.copy()
    result[c] = result[a] + b
    return result


def mulr(a, b, c):
    result = registers.copy()
    result[c] = result[a] * result[b]
    return result


def muli(a, b, c):
    result = registers.copy()
    result[c] = result[a] * b
    return result


def banr(a, b, c):
    result = registers.copy()
    result[c] = result[a] & result[b]
    return result


def bani(a, b, c):
    result = registers.copy()
    result[c] = result[a] & b
    return result


def borr(a, b, c):
    result = registers.copy()
    result[c] = result[a] | result[b]
    return result


def bori(a, b, c):
    result = registers.copy()
    result[c] = result[a] | b
    return result


def setr(a, b, c):
    result = registers.copy()
    result[c] = result[a]
    return result


def seti(a, b, c):
    result = registers.copy()
    result[c] = a
    return result


def gtir(a, b, c):
    result = registers.copy()
    result[c] = 1 if a > result[b] else 0
    return result


def gtri(a, b, c):
    result = registers.copy()
    result[c] = 1 if result[a] > b else 0
    return result


def gtrr(a, b, c):
    result = registers.copy()
    result[c] = 1 if result[a] > result[b] else 0
    return result


def eqir(a, b, c):
    result = registers.copy()
    result[c] = 1 if a == result[b] else 0
    return result


def eqri(a, b, c):
    result = registers.copy()
    result[c] = 1 if result[a] == b else 0
    return result


def eqrr(a, b, c):
    result = registers.copy()
    result[c] = 1 if result[a] == result[b] else 0
    return result


operations = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

ordered_operations = [None] * 16

line = "start"
while line:
    registers = list(map(lambda x: int(x), regex.findall(file.readline())))
    operation = list(map(lambda x: int(x), regex.findall(file.readline())))
    after = list(map(lambda x: int(x), regex.findall(file.readline())))

    matching_ops = 0
    for op in operations:
        if op(operation[1], operation[2], operation[3]) == after:
            if ordered_operations[operation[0]] is None:
                ordered_operations[operation[0]] = []

            if op not in ordered_operations[operation[0]]:
                ordered_operations[operation[0]].append(op)
        elif ordered_operations[operation[0]] is not None and op in ordered_operations[operation[0]]:
            ordered_operations[operation[0]].remove(op)

    line = file.readline()

# pprint(ordered_operations)

progress = True
while progress:
    progress = False
    for valid_ops in ordered_operations.copy():
        if len(valid_ops) == 1:
            for ops in ordered_operations:
                if len(ops) > 1 and valid_ops[0] in ops:
                    ops.remove(valid_ops[0])
                    progress = True

pprint(ordered_operations)

registers = [0, 0, 0, 0]

file = open("input2.txt", 'r')
for line in file.readlines():
    operation = list(map(lambda x: int(x), regex.findall(line)))
    registers = ordered_operations[operation[0]][0](operation[1], operation[2], operation[3])

print(registers)
