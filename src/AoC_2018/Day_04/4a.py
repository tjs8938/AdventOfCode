#!/bin/python

import re
import pprint
from datetime import datetime

file = open("input.txt", 'r')
lines = file.readlines()

def parseDateTime(line):
    pattern = re.compile("\[([^\]]*).*")
    timestamp = pattern.match(line).group(1)
    return datetime.strptime(timestamp, "%Y-%m-%d %H:%M")

lines.sort(key=lambda line: parseDateTime(line))

maxGuard = ""
currentGuard = ""
maxMinute = 0
maxOccurs = 0
start_min = 0


guards = {}

regex = re.compile(".*:([0-9]*)\] (\w*) #?(\w*)")
for line in lines:
    m = regex.match(line)
    minute = m.group(1)
    action = m.group(2)
    id = m.group(3)

    if action == "Guard":
        currentGuard = str(id)
        if id not in guards:
            guards[currentGuard] = {}
    elif action == "falls":
        start_min = int(minute)
    elif action == "wakes":
        for i in range(start_min, int(minute)):
            if str(i) not in guards[currentGuard]:
                guards[currentGuard][str(i)] = 0
            guards[currentGuard][str(i)] += 1
            if guards[currentGuard][str(i)] > maxOccurs:
                maxOccurs = guards[currentGuard][str(i)]
                maxGuard = currentGuard
                maxMinute = i

print (maxMinute)
print (maxGuard)
print (maxMinute * int(maxGuard))