#!/bin/python

import re
from pprint import pprint

parts = []

for i in range(26):
    parts.append(list())

file = open("input.txt", 'r')

lines = file.readlines()

pattern = re.compile("Step ([A-Z]) must be finished before step ([A-Z]) can begin.")
for line in lines:
    m = pattern.match(line)
    index = ord(m.group(2)) - ord('A')
    if len(parts) <= index:
        parts.index(list(), index)

    parts[index].append(m.group(1))


for i in range(len(parts)):
    print (chr(ord('A') + i), parts[i])

output = ""
progress = True
while progress:
    progress = False
    for i in range(len(parts)):
        if len(parts[i]) == 0:
            letter = chr(ord('A') + i)
            parts[i].append('DONE')
            output += letter
            progress = True
            for j in range(len(parts)):
                if letter in parts[j]:
                    parts[j].remove(letter)
            break

print(output)



exit(0)
