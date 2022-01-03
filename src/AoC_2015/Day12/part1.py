import re

filename = "input.txt"
# filename = "test1.txt"

file = open(filename)
input_lines = file.read().splitlines()
number = re.compile("([-+]?[0-9]+)")

total = 0
num_strings = number.findall(input_lines[0])
for s in num_strings:
    total += int(s)

print(total)
