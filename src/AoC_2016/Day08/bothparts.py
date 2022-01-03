import re
from typing import List

# inputs = open("test1.txt").read().splitlines()
from src.Utility.MatrixPrint import print_matrix


def process_rules(width=50, height=6, filename="input.txt"):
    inputs = open(filename).read().splitlines()

    grid = []
    for i in range(height):
        list = []
        for j in range(width):
            list.append('.')
        grid.append(list)

    # print_matrix(grid)

    pattern = re.compile("(rotate|rect) (row|column)?.*?([0-9]+).*?([0-9]+)")
    for line in inputs:
        print(line)
        m = pattern.match(line)
        if m.group(1) == "rect":
            x = int(m.group(3))
            y = int(m.group(4))

            for i in range(y):
                for j in range(x):
                    grid[i][j] = '#'
        else:
            if m.group(2) == "row":
                y = int(m.group(3))
                shift = int(m.group(4))
                new_list = grid[y][shift * -1:]
                new_list.extend(grid[y][:shift * -1])
                grid[y] = new_list
            else:
                x = int(m.group(3))
                shift = int(m.group(4))

                column = ""
                for i in range(height):
                    column += grid[i][x]

                for i in range(height):
                    grid[(shift + i) % height][x] = column[i]

        print_matrix(grid)
        print("\n-----------------------------------------------------------------\n")

    count_on = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == '#':
                count_on += 1

    print(count_on)


process_rules(width=7, height=3, filename="test1.txt")
process_rules()
