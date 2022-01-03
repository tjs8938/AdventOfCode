#!/bin/python

import re

file = open("input.txt", 'r')

polymer = file.readline()

madeProgress = True

while len(polymer) > 0 and madeProgress:
    madeProgress = False

    i = 0
    while i < len(polymer)-1:
        diff = ord(polymer[i]) - ord(polymer[i+1])
        if abs(diff) == 32:
            madeProgress = True
            polymer = polymer[:i] + polymer[i+2:]
            if i > 0:
                i -= 1

        else:
            i += 1

print(len(polymer))
print (polymer)



