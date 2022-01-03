#!/bin/python

import re
from pprint import pprint

file = open("input.txt", 'r')

pattern = re.compile("[0-9]+")
numbers = pattern.findall(file.readline())

total = 0

def parseNode(index):
    numChildren = int(numbers[index])
    index += 1
    numMeta = int(numbers[index])
    index += 1
    for i in range(numChildren):
        index = parseNode(index)

    for i in range(numMeta):
        global total
        total += int(numbers[index])
        index += 1

    return index

parseNode(0)
print (total)
