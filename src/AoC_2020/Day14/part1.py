import re

input_file = open("input.txt")
# input_file = open("test1.txt")
input_lines = input_file.read().splitlines()

and_mask = 0
or_mask = 0

registers = {}


def process_mask(mask):
    global and_mask, or_mask
    and_mask = 0
    or_mask = 0
    for c in mask:
        and_mask *= 2
        or_mask *= 2
        and_mask += 0 if c == '0' else 1
        or_mask += 1 if c == '1' else 0
    pass


for line in input_lines:
    m = re.match("mask = (.*)", line)
    if m is not None:
        process_mask(m.group(1))
        continue

    m = re.match("mem\\[([0-9]*)\\] = ([0-9]*)", line)
    addr = m.group(1)
    value = (int(m.group(2)) & and_mask) | or_mask
    registers[addr] = value

total = 0
for v in registers.values():
    total += v

print(total)
