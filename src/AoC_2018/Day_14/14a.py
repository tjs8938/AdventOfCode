#!/bin/python

from pprint import pprint
import re

NUM_RECIPES = 640441

elves = [0, 1]

scores = [3, 7]

while len(scores) < NUM_RECIPES + 10:
    total = 0
    for elf in elves:
        total += scores[elf]

    for char in str(total):
        scores.append(int(char))

    for i in range(len(elves)):
        elves[i] = (elves[i] + scores[elves[i]] + 1) % len(scores)

print(scores[NUM_RECIPES:NUM_RECIPES+10])