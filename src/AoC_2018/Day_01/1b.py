#!/bin/python


current = 0
valuesSeen = []

while True:
    file = open("input.txt", 'r')
    for line in file:
        current += int(line)
        if current in valuesSeen:
            print(current)
            break
        valuesSeen.append(current)
