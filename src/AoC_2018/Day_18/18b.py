#!/bin/python
from pprint import pprint

file = open("input.txt", 'r')

forest = file.read().split('\n')

MINUTES = 1000000000

all_forests = []
new_forest = []

first_match = None

fmi = 0
nmi = 0

keep_going = True
i = 0
while keep_going:
    for row in range(len(forest)):
        new_row = ""
        for acre in range(len(forest[row])):
            forest_square = ""

            if acre > 0:
                forest_square += forest[row][acre - 1]

            if acre < len(forest[row]) - 1:
                forest_square += forest[row][acre + 1]

            if row > 0:
                forest_square += forest[row - 1][max(acre - 1, 0):min(acre + 1, len(forest[row - 1]) - 1) + 1]

            if row < len(forest) - 1:
                forest_square += forest[row + 1][max(acre - 1, 0):min(acre + 1, len(forest[row + 1]) - 1) + 1]

            if forest[row][acre] == '.':
                new_row += ('|' if forest_square.count('|') >= 3 else '.')
            elif forest[row][acre] == '|':
                new_row += ('#' if forest_square.count('#') >= 3 else '|')
            else:
                new_row += ('#' if forest_square.count('#') >= 1 and forest_square.count('|') >= 1 else '.')

        new_forest.append(new_row)

    forest = new_forest
    if forest in all_forests and first_match is None:
        print(i)
        pprint(forest)
        first_match = forest
        fmi = i
    elif first_match == forest:
        print(i)
        nmi = i
    elif first_match is not None and nmi > 0 and (MINUTES - i - 1) % (nmi - fmi) == 0:
        print(i)
        break
    else:
        all_forests.append(forest)
    new_forest = []
    i += 1

woods = 0
lumberyards = 0
for row in forest:
    woods += row.count('|')
    lumberyards += row.count('#')

print(woods, lumberyards, woods * lumberyards)
