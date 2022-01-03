import re

filename = "input.txt"
# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
tree_product = 1

for slope in slopes:
    trees = 0
    horizontal = 0
    vertical = 0

    while vertical < len(input_lines):
        line = input_lines[vertical]
        if line[horizontal] == '#':
            trees += 1
        horizontal = (horizontal + slope[0]) % len(line)
        vertical = vertical + slope[1]

    tree_product = tree_product * trees

print(tree_product)

