import re
from typing import List

dance_moves: List[str] = open("input.txt").read().split(',')
program_line = list('abcdefghijklmnop')


def spin(arg: int):
    global program_line
    program_line = program_line[-arg:] + program_line[:-arg]


def exchange(a: int, b:int):
    global program_line
    swap = program_line[a]
    program_line[a] = program_line[b]
    program_line[b] = swap


def partner(a: str, b: str):
    a_idx = program_line.index(a)
    b_idx = program_line.index(b)
    return exchange(a_idx, b_idx)


pattern = re.compile('([xsp])([a-p0-9]*)/?([a-p0-9]*)?')


for move in dance_moves:
    m = pattern.match(move)
    if m.group(1) == 's':
        spin(int(m.group(2)))
    elif m.group(1) == 'x':
        exchange(int(m.group(2)), int(m.group(3)))
    else:
        partner(m.group(2), m.group(3))

print(''.join(program_line))
