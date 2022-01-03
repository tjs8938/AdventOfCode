#!/bin/python
import re
from pprint import pprint

file = open("input.txt", 'r')

STEPS = 122

# 120: 8040
# 121: 8107
# 122: 8174

init_state = re.compile("initial state: (.*)")
rule = re.compile("([.#]{5}) => ([.#])")

plants = ""
rules = {}
for line in file.readlines():
    if init_state.match(line):
        plants = init_state.match(line).group(1)
    elif rule.match(line):
        m = rule.match(line)
        rules[m.group(1)] = m.group(2)

print(plants)
pprint(rules)

for i in range(STEPS):
    old_plants = '...' + plants + '...'
    plants = ''
    for j in range(len(old_plants) - 4):
        plants += rules[old_plants[j:j+5]]

    print(plants[i:])

total = 0
for i in range(len(plants)):
    if plants[i] == '#':
        total += i - STEPS

print(total)
