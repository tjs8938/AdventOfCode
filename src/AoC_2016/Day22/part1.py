import itertools
import re
from typing import Tuple, List, Dict

from src.Utility.MatrixPrint import position_to_key

pattern = re.compile("/dev/grid/node-x(?P<x>\\d*)-y(?P<y>\\d*)\\W*(?P<size>\\d*)T\\W*(?P<used>\\d*)T\\W*(?P<avail>\\d*)T\\W*(?P<use_perc>\\d*)%")

nodes: Dict[str, Dict[str, int]] = {}
for input_line in open("input.txt").read().splitlines():
    m = pattern.match(input_line)
    if m is not None:
        node = m.groupdict()
        node = dict((k, int(v)) for k, v in node.items())
        nodes[position_to_key(node['x'], node['y'])] = node

part1 = 0
for pair in itertools.permutations(nodes.values(), 2):
    if 0 < pair[0]['used'] <= pair[1]['avail']:
        part1 += 1

print(part1)