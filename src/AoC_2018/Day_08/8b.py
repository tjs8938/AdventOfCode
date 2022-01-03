#!/bin/python

import re
from pprint import pprint

file = open("input.txt", 'r')

pattern = re.compile("[0-9]+")
numbers = pattern.findall(file.readline())

total = 0
index = 0


class Node:
    def __init__(self):
        self.children = []
        self.meta = 0


def getNumber():
    global index
    retVal = int(numbers[index])
    index += 1
    return retVal


def parseNode():
    numChildren = getNumber()
    numMeta = getNumber()
    node = Node()
    for i in range(numChildren):
        node.children.append(parseNode())

    for i in range(numMeta):
        meta = getNumber()
        if len(node.children) == 0:
            node.meta += meta
        elif len(node.children) >= meta:
            node.meta += node.children[meta - 1].meta

    return node


node = parseNode()
print(node.meta)
