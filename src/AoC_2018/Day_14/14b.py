#!/bin/python

from pprint import pprint
import re

TARGET = "640441"

elves = [0, 1]

scores = "37"

found_it = False
while not found_it:
    total = 0
    for elf in elves:
        total += int(scores[elf])

    for char in str(total):
        scores += char
        if scores[len(TARGET) * -1:] == TARGET:
            # print(scores)
            print(len(scores) - len(TARGET))
            exit(0)

    for i in range(len(elves)):
        elves[i] = (elves[i] + int(scores[elves[i]]) + 1) % len(scores)
