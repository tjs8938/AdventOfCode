import re
import string

filename = "input.txt"

# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()

find_hex = re.compile("\\\\x[0-9a-fA-F]{2}")
find_escapes_and_quotes = re.compile("(\\\"|\\\\)")

diff = 0


def process_string(line):
    START = 0
    SLASH = 1
    X = 2
    HEX = 3

    current_state = START
    diff = 0
    for c in line:
        if current_state == START:
            if c == '\\':
                current_state = SLASH
        elif current_state == SLASH:
            if c in ['\\', '"']:
                diff += 1
                current_state = START
            elif c == 'x':
                current_state = X
            else:
                current_state = START
        elif current_state == X:
            if c in string.hexdigits:
                current_state = HEX
            else:
                current_state = START
        else:
            if c in string.hexdigits:
                diff += 3
            current_state = START

    return diff


for line in input_lines:
    # remove (and count) outer quotes
    diff += 2
    line = line[1:-1]

    # remove (and count) escaped quotes and slashes
    diff += process_string(line)

print(diff)
