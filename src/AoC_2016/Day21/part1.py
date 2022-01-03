import re
from typing import Tuple, List

pattern = re.compile("(move|rotate|swap|reverse) ((positions?|letter) (\\w*) (with|to|through) ((position|letter) )?(\\w*)|(based on position of letter|left|right) (\\w*))")


def move(m, pw: str):
    x = int(m.group(4))
    y = int(m.group(8))
    char = pw[x]
    pw = pw[:x] + pw[x + 1:]
    pw = pw[:y] + char + pw[y:]
    return pw


def reverse(m, pw: str):
    x = int(m.group(4))
    y = int(m.group(8))
    pw = pw[:x] + pw[x:y + 1][::-1] + pw[y + 1:]
    return pw


def swap(m, pw: str):
    sub_command = m.group(3)
    index_1 = m.group(4)
    index_2 = m.group(8)
    if sub_command == 'position':
        x = int(index_1)
        y = int(index_2)
    else:
        x = pw.index(index_1)
        y = pw.index(index_2)

    if x > y:
        x, y = y, x
    x_val = pw[x]
    y_val = pw[y]
    pw = pw[:x] + y_val + pw[x + 1:y] + x_val + pw[y + 1:]
    return pw


def rotate(m, pw: str):
    sub_command = m.group(9)
    param = m.group(10)
    if sub_command == 'left':
        shift = int(param)
    elif sub_command == 'right':
        shift = -1 * int(param)
    else:
        index = pw.index(param)
        shift = -1 * ((index + (1 if index < 4 else 2)) % len(pw))

    pw = pw[shift:] + pw[:shift]

    return pw


def scramble(password: str, filename: str) -> str:
    input_lines = open(filename).read().splitlines()
    length = len(password)
    steps = []
    for line in input_lines:
        match = pattern.match(line)
        command = match.group(1)
        password = eval(command)(match, password)
        assert(len(password) == length)
        steps.append(password)
    print(steps[::-1])
    return password


print(scramble('abcde', 'test1.txt'))
print(scramble('abcdefgh', 'input.txt'))
