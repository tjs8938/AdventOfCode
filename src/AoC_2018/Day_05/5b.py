#!/bin/python

import re

def reducePolymer(letter):
    file = open("input.txt", 'r')

    polymer = file.readline().replace(letter, '').replace(chr(ord(letter)-32), '')

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

    return len(polymer)

shortestLength = 500000
shortestLetter = ""
for i in range(0,27):
    letter = chr(ord('a')+i)
    length = reducePolymer(letter)
    if length < shortestLength:
        shortestLength = length
        shortestLetter = letter

print(shortestLength)
print (shortestLength)
