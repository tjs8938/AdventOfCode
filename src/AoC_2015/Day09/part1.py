import itertools
import re

pattern = re.compile("([^ ]*) to ([^ ]*) = ([0-9]*)")

filename = "input.txt"
# filename = "test1.txt"

file = open(filename)
input_lines = file.read().splitlines()

distances = {}

for line in input_lines:
    m = pattern.match(line)
    start = m.group(1)
    end = m.group(2)
    dist = int(m.group(3))
    if start not in distances:
        distances[start] = {}
    if end not in distances:
        distances[end] = {}
    distances[start][end] = dist
    distances[end][start] = dist

print(distances)

all_routes = []
for combo in itertools.permutations(distances.keys()):
    dist = 0
    for i in range(0, len(combo) - 1):
        dist += distances[combo[i]][combo[i+1]]
    print(combo, dist)
    all_routes.append(dist)

print(min(all_routes))
print(max(all_routes))
