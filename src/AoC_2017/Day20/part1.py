import re
from typing import List, Tuple

pattern = re.compile('p=<([-0-9]*),([-0-9]*),([-0-9]*)>, v=<([-0-9]*),([-0-9]*),([-0-9]*)>, a=<([-0-9]*),([-0-9]*),([-0-9]*)>')

particle_input = open('input.txt').read().splitlines()

particles: List[Tuple[int, int, int]] = []

for p in particle_input:
    m = pattern.match(p)
    particles.append((int(m.group(7)), int(m.group(8)), int(m.group(9))))

lowest = 0
lowest_val = pow(2, 31)
for i in range(len(particles)):
    p = particles[i]
    a = abs(p[0]) + abs(p[1]) + abs(p[2])
    if a < lowest_val:
        lowest = i
        lowest_val = a

print(lowest)