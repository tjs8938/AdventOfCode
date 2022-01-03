import re
from typing import Set

input_file = open("input.txt")
# input_file = open("test1.txt")
input_lines = input_file.read().splitlines()

occurrence_count = {}
potential_allergens = {}
known_allergens = {}

split = re.compile("(.*) \\(contains (.*)\\)")

for line in input_lines:
    m = split.match(line)
    ingredients = m.group(1).split()
    allergens = m.group(2).split(', ')
    for a in allergens:
        if a not in potential_allergens:
            potential_allergens[a] = set(ingredients)
        else:
            potential_allergens[a] = potential_allergens[a].intersection(set(ingredients))

    for i in ingredients:
        if i not in occurrence_count:
            occurrence_count[i] = 0
        occurrence_count[i] += 1

# print(occurrence_count)
# print("Potential: " + str(potential_allergens))
# print("Known: " + str(known_allergens))
# print()


while len(potential_allergens) > 0:
    known = {k: v for k, v in potential_allergens.items() if len(v) == 1}
    potential_allergens = {k: v for k, v in potential_allergens.items() if len(v) != 1}

    v: Set[str]
    for k, v in known.items():
        ingredient = v.pop()
        known_allergens[ingredient] = k
        p: Set[str]
        for p in potential_allergens.values():
            if ingredient in p:
                p.discard(ingredient)

    # print("Potential: " + str(potential_allergens))
    # print("Known: " + str(known_allergens))
    # print()

total = 0
for i in occurrence_count:
    if i not in known_allergens:
        total += occurrence_count[i]

print("Part 1: " + str(total))

known_allergens = dict(sorted(known_allergens.items(), key=lambda item: item[1]))
print("Part 2: " + ','.join(known_allergens.keys()))
