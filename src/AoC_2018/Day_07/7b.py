#!/bin/python

import re
from pprint import pprint

NUM_WORKERS = 5
DELAY = 60
STEPS = 26


parts = []

for i in range(STEPS):
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
    print(chr(ord('A') + i), parts[i])

jobs = {}

seconds = -1
output = ""
while len(output) < STEPS:

    print(jobs)
    for job in jobs.copy().keys():
        jobs[job] -= 1
        if jobs[job] == 0:
            jobs.pop(job)
            index = ord(job) - ord('A')
            output += job
            for j in range(len(parts)):
                if job in parts[j]:
                    parts[j].remove(job)

    progress = True
    while len(jobs) < NUM_WORKERS and progress:
        progress = False
        for i in range(len(parts)):
            if len(parts[i]) == 0:
                parts[i].append('DONE')
                progress = True
                letter = chr(ord('A') + i)
                jobs[letter] = i + DELAY + 1
                break
    seconds += 1

print(output)
print (seconds)



exit(0)
