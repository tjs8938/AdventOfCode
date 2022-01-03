#!/bin/python

file = open("input.txt", 'r')

lines = file.readlines()
lines.sort()

for a, b in zip(lines[:-1], lines[1:]):
    diff_count = 0
    for i in range(0, len(a)-1):
        if a[i] != b[i]:
            diff_count += 1

    if diff_count == 1:
        print (a, b)
        exit(0)
