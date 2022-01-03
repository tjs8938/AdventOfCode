import re
from typing import Dict

# filename = "test1.txt"
filename = "input.txt"


input_line = open(filename).read().splitlines()

pattern = re.compile('(.*) \\(([0-9]*)\\)( -> (.*))?')


class Program:

    def __init__(self, name: str):
        self.name = name
        self.parent: Program = None
        self.weight = -1


programs: Dict[str, Program] = {}

for line in input_line:
    m = pattern.match(line)
    name = m.group(1)
    if name not in programs:
        programs[name] = Program(name)
    prog = programs[name]
    prog.weight = int(m.group(2))

    if m.group(4):
        children = m.group(4).split(', ')
        for c in children:
            if c not in programs:
                programs[c] = Program(c)
            child = programs[c]
            child.parent = prog

bottom = prog
while bottom.parent:
    bottom = bottom.parent

print(bottom.name)