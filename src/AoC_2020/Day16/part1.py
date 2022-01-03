import re
from functools import reduce
from typing import List

constraint_pattern = re.compile("^(.*): ([0-9]*)-([0-9]*) or ([0-9]*)-([0-9]*)")
ticket_pattern = re.compile("([0-9]+)")

# constraint_file = open("test_constraints.txt")
constraint_file = open("constraints.txt")
#
# ticket_file = open("test_tickets.txt")
ticket_file = open("tickets.txt")


class Constraint:

    def __init__(self, name: str, bounds: List[int]):
        self.bounds = bounds
        self.name = name
        self.validate = lambda x: self.bounds[0] <= x <= self.bounds[1] or self.bounds[2] <= x <= self.bounds[3]


constraints = []
for line in constraint_file.read().splitlines():
    m = constraint_pattern.match(line)
    constraints.append(Constraint(m.group(1), list(map(lambda x: int(x), m.groups()[1:]))))


total = 0
for line in ticket_file.read().splitlines():
    for value in map(lambda x: int(x), ticket_pattern.findall(line)):
        total += (0 if reduce(lambda a, b: a or b, map(lambda c: c.validate(value), constraints)) else value)

print(total)
