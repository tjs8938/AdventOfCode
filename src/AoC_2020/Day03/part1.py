import re

filename = "input.txt"
# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()

trees = 0
horizontal = 0

for line in input_lines:
    if line[horizontal] == '#':
        trees += 1
    horizontal = (horizontal + 3) % len(line)

print(trees)

