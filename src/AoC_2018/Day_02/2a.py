#!/bin/python

file = open("input.txt", 'r')
start = 0

twoCounts = 0
threeCounts = 0

for line in file:
    letter_counts = {}
    for letter in line:
        if letter not in letter_counts:
            letter_counts[letter] = 0
        letter_counts[letter] += 1

    if 2 in letter_counts.values():
        twoCounts += 1

    if 3 in letter_counts.values():
        threeCounts += 1

print(twoCounts * threeCounts)