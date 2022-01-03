import re
from typing import Dict, List

filename = "test1.txt"
# filename = "input.txt"


input_line = open(filename).read().splitlines()

pattern = re.compile('(.*) \\(([0-9]*)\\)( -> (.*))?')


class Program:

    def __init__(self, name: str):
        self.name = name
        self.parent: Program = None
        self.weight = -1
        self.total_weight = -1
        self.children: List[Program] = []

    def get_weight(self):
        if self.total_weight == -1:
            self.total_weight = self.weight
            for c in self.children:
                self.total_weight += c.get_weight()

        return self.total_weight


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
            prog.children.append(child)

bottom = prog
while bottom.parent:
    bottom = bottom.parent


def find_unbalanced(prog: Program, target_weight: int):
    weights: Dict[int, List[Program]] = {}

    for c in prog.children:
        w = c.get_weight()
        if w not in weights:
            weights[w] = []
        weights[w].append(c)

    if len(weights) == 1:
        # All children weigh the same amount, so this program is the one that is mis-labeled
        w = weights.popitem()
        print(target_weight - prog.get_weight() + prog.weight)
        exit(0)
    else:
        new_target = 0
        child = None
        for w, l in weights.items():
            if len(l) == 1:
                child = l[0]
            else:
                new_target = l[0].get_weight()

        find_unbalanced(child, new_target)


find_unbalanced(bottom, 0)
