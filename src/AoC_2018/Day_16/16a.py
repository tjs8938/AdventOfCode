#!/bin/python
import re

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

answer = 0

line = "start"
while line:
    registers = list(map(lambda x: int(x), regex.findall(file.readline())))
    operation = list(map(lambda x: int(x), regex.findall(file.readline())))
    after = list(map(lambda x: int(x), regex.findall(file.readline())))

    matching_ops = 0
    for op in operations:
        if op(operation[1], operation[2], operation[3]) == after:
            matching_ops += 1

    if matching_ops >= 3:
        answer += 1

    line = file.readline()

print(answer)