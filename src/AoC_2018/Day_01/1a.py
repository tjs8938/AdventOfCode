#!/bin/python

file = open("input.txt", 'r')
start = 0

for line in file:
    start += int(line)

print(start)