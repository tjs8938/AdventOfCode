import re

filename = "input.txt"
# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()

REGEX = "^([0-9]*)-([0-9]*) (.): (.*)"
valid = 0

for line in input_lines:
    m = re.search(REGEX, line)
    low = int(m.group(1))
    high = int(m.group(2))
    char = m.group(3)
    pw = m.group(4)
    count = pw.count(char)
    if low <= count <= high:
        valid += 1

print(valid)
