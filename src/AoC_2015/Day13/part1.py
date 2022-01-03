import itertools
import re

filename = "input.txt"
# filename = "test1.txt"

file = open(filename)
input_lines = file.read().splitlines()
pattern = re.compile("(.*) would (gain|lose) ([0-9]*) happiness units by sitting next to (.*).")

values = {}

for line in input_lines:
    m = pattern.match(line)
    p1 = m.group(1)
    p2 = m.group(4)
    amount = int(m.group(3)) * (1 if m.group(2) == 'gain' else -1)

    if p1 not in values:
        values[p1] = {}
    values[p1][p2] = amount


values['Tom'] = {}
for pers in values.keys():
    values['Tom'][pers] = 0
    values[pers]['Tom'] = 0


print(values)


best_happiness = 0
best_perm = None
for perms in itertools.permutations(values.keys()):
    happiness = 0
    for i in range(len(perms)):
        p1 = perms[i]
        p2 = perms[(i + 1) % len(perms)]
        happiness += values[p1][p2]
        happiness += values[p2][p1]

    if happiness > best_happiness:
        best_happiness = happiness
        best_perm = perms

print(best_happiness)
