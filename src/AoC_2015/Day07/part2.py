filename = "input.txt"
import re

# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()

split_regex = re.compile("(.*) -> (.*)")
constant = re.compile("^([^ ]*)$")
unary = re.compile("(NOT) (.*)")
binary = re.compile("(.*) (AND|OR|LSHIFT|RSHIFT) (.*)")


class Wire:

    def __init__(self, value):
        self.value = value
        self.signal = -1


wires = {}
for line in input_lines:
    m = split_regex.match(line)
    wires[m.group(2)] = Wire(m.group(1))


def NOT(operand):
    return operand ^ 0xFFFF


def AND(op1, op2):
    return op1 & op2


def OR(op1, op2):
    return op1 | op2


def RSHIFT(op1, op2):
    return op1 >> op2


def LSHIFT(op1, op2):
    return op1 << op2


def calc(wire_name):
    wire = wires[wire_name]
    if wire.signal > -1:
        return wire.signal

    # This wire hasn't been computed yet, so... do that
    m = constant.match(wire.value)
    if m is not None:
        operand = m.group(1)
        wire.signal = resolve_operand(operand)
        return wire.signal

    m = unary.match(wire.value)
    if m is not None:
        operation = m.group(1)
        operand = m.group(2)
        value = resolve_operand(operand)
        wire.signal = eval(operation)(value)
        return wire.signal

    m = binary.match(wire.value)
    if m is not None:
        operand1 = resolve_operand(m.group(1))
        operation = m.group(2)
        operand2 = resolve_operand(m.group(3))

        wire.signal = eval(operation)(operand1, operand2)
        return wire.signal


def resolve_operand(operand):
    if operand.isnumeric():
        value = int(operand)
    else:
        value = calc(operand)
    return value


new_b = calc('a')

for name, wire in wires.items():
    wire.signal = new_b if name == 'b' else -1

print(calc('a'))
