import collections
from copy import deepcopy
from functools import reduce
from typing import List, Dict, Set


class Component:

    def __init__(self, label: str):
        self.label = label
        port_strs = label.split('/')
        self.port1 = int(port_strs[0])
        self.port2 = int(port_strs[1])

    def __repr__(self):
        return self.label

    def __eq__(self, other):
        return self.label == other.label

    def __hash__(self):
        return self.label.__hash__()

    def other_port(self, port_val):
        return self.port1 if port_val == self.port2 else self.port2

    def __int__(self):
        return self.port1 + self.port2


class Path:

    def __init__(self):
        self.ports: List[Component] = []
        self.next_val: int = None
        self.strength = 0

    def __repr__(self):
        return '(' + str(reduce(lambda a, b: str(a) + ', ' + str(b), self.ports)) + ') - ' + str(self.next_val)

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def add_component(self, c: Component):
        self.ports.append(c)
        self.strength += c.port1 + c.port2
        self.next_val = c.other_port(self.next_val)

    def get_strength(self):
        return self.strength


# filename = "test1.txt"
filename = "input.txt"
input_lines = open(filename).read().splitlines()

components: Dict[int, Set[Component]] = {}
for line in input_lines:
    c = Component(line)
    if c.port1 not in components:
        components[c.port1] = set()
    components[c.port1].add(c)

    if c.port2 not in components:
        components[c.port2] = set()
    components[c.port2].add(c)


# List of paths to be processed
paths = collections.deque()
for c in components[0]:
    new_path = Path()
    new_path.next_val = 0
    new_path.add_component(c)
    paths.append(new_path)

# Paths that came to an end and could not grow longer
seen_paths = set()
completed_paths = set()
while (len(paths)) > 0:
    current_path = paths.popleft()
    new_paths = []
    for c in components[current_path.next_val]:
        if c not in current_path.ports:
            p = deepcopy(current_path)
            p.add_component(c)
            new_paths.append(p)
    if len(new_paths) == 0:
        completed_paths.add(current_path)
    else:
        for path in new_paths:
            if path not in seen_paths:
                paths.append(path)
                seen_paths.add(path)

# print(seen_paths)
best = 0
best_path = None
for p in completed_paths:
    value = p.get_strength()
    if value > best:
        best = value
        best_path = p

print('Part 1: ', best)

best_len = 0
best_strength = 0
best_path = None
for p in completed_paths:
    if len(p.ports) > best_len or (len(p.ports) == best_len and p.get_strength() > best_strength):
        best_len = len(p.ports)
        best_strength = p.get_strength()
        best_path = p

print('Part 2: ', best_strength)