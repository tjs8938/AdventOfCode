#!/bin/python

import re

file = open("input.txt", 'r')

numbers = re.compile('[0-9]+')

squares = {}
for line in file:
    params = numbers.findall(line)
    x = int(params[1])
    y = int(params[2])
    w = int(params[3])
    h = int(params[4])

    for i in range(x, x+w):

        if i not in squares:
            squares[i] = {}

        for j in range(y, y+h):
            if j not in squares[i]:
                squares[i][j] = 0

            squares[i][j] += 1

file = open("input.txt", 'r')

def search_line(line):
    params = numbers.findall(line)
    index = int(params[0])
    x = int(params[1])
    y = int(params[2])
    w = int(params[3])
    h = int(params[4])


    for i in range(x, x+w):
        for j in range(y, y+h):
            if squares[i][j] != 1:
                return
    print(index)

for line in file:
    search_line(line)
