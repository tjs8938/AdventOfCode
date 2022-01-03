import re

input_file = open("input.txt")
# input_file = open("test1.txt")
input_lines = input_file.read().splitlines()

registers = {}

mask = ""


def process_mask(addr, mask):
    addr_string = format(addr, '036b')
    result = ""
    for pair in zip(addr_string, mask):
        if pair[1] == 'X':
            result += 'X'
        elif pair[1] == '0':
            result += pair[0]
        else:
            result += '1'
    return result


def set_value(addr_mask, value):
    if addr_mask.count('X') == 0:
        registers[addr_mask] = value
    else:
        zero = addr_mask.replace('X', '0', 1)
        one = addr_mask.replace('X', '1', 1)
        set_value(zero, value)
        set_value(one, value)
    pass


for line in input_lines:
    m = re.match("mask = (.*)", line)
    if m is not None:
        mask = m.group(1)
        continue

    m = re.match("mem\\[([0-9]*)\\] = ([0-9]*)", line)
    addr = int(m.group(1))
    addr_mask = process_mask(addr, mask)
    set_value(addr_mask, int(m.group(2)))

total = 0
for v in registers.values():
    total += v

print(total)
