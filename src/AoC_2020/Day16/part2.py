import re
from functools import reduce
from typing import List, Set

constraint_pattern = re.compile("^(.*): ([0-9]*)-([0-9]*) or ([0-9]*)-([0-9]*)")
ticket_pattern = re.compile("([0-9]+)")

# constraint_file = open("test2_constraints.txt")
constraint_file = open("constraints.txt")
#
# ticket_file = open("test2_tickets.txt")
ticket_file = open("tickets.txt")


class Constraint:

    def __init__(self, name: str, bounds: List[int]):
        self.bounds = bounds
        self.name = name
        self.validate = lambda x: self.bounds[0] <= x <= self.bounds[1] or self.bounds[2] <= x <= self.bounds[3]

    def __repr__(self):
        return self.name


constraints: List[Constraint] = []
for line in constraint_file.read().splitlines():
    m = constraint_pattern.match(line)
    constraints.append(Constraint(m.group(1), list(map(lambda x: int(x), m.groups()[1:]))))


class Ticket:

    def __init__(self, values: List[int]):
        self.values = values
        self.fields: List[Set[Constraint]] = []

        for v in values:
            self.fields.append(set())
            for c in constraints:
                if c.validate(v):
                    self.fields[-1].add(c)

    def __repr__(self):
        return str(self.fields)


tickets: List[Ticket] = []
for line in ticket_file.read().splitlines():
    t = Ticket(list(map(lambda x: int(x), ticket_pattern.findall(line))))
    if reduce(lambda a, b: a or b, map(lambda s: len(s) == 0, t.fields)):
        continue
    tickets.append(t)

print(tickets)

possible_values: List[Set[Constraint]] = tickets[0].fields.copy()

for i in range(1, len(tickets)):
    for j in range(len(possible_values)):
        possible_values[j] = possible_values[j].intersection(tickets[i].fields[j])

print(possible_values)
definite_values: List[Constraint] = [None] * len(possible_values)
while reduce(lambda a, b: a or b, map(lambda x: x is None, definite_values)):
    for i in range(len(definite_values)):
        if len(possible_values[i]) == 1:
            definite_values[i] = possible_values[i].pop()
            for j in range(len(possible_values)):
                if i != j and definite_values[i] in possible_values[j]:
                    possible_values[j].discard(definite_values[i])

print(definite_values)

my_ticket = [157, 73, 79, 191, 113, 59, 109, 61, 103, 101, 67, 193, 97, 179, 107, 89, 53, 71, 181, 83]

product = 1
for i in range(len(definite_values)):
    if definite_values[i].name.startswith("departure"):
        product *= my_ticket[i]

print(product)
