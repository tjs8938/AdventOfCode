#!/bin/python
import re

file = open("input.txt", 'r')

regex = re.compile('([a-z]+) ([0-9]+) ([0-9]+) ([0-9]+)')


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


ip_reg = 4

registers = [0, 0, 0, 0, 0, 0]

instructions = file.readlines()

ip = 0

while ip < len(instructions):
    registers[ip_reg] = ip
    m = regex.match(instructions[ip])
    print(m.group(1))
    registers = eval(m.group(1))(int(m.group(2)), int(m.group(3)), int(m.group(4)))
    ip = registers[ip_reg] + 1

print(registers)