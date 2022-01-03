from __future__ import annotations

import itertools
import math
import re
from typing import List

pattern = re.compile('p=<(?P<px>[-0-9]*),(?P<py>[-0-9]*),(?P<pz>[-0-9]*)>, '
                     'v=<(?P<vx>[-0-9]*),(?P<vy>[-0-9]*),(?P<vz>[-0-9]*)>, '
                     'a=<(?P<ax>[-0-9]*),(?P<ay>[-0-9]*),(?P<az>[-0-9]*)>')

particle_input = open('input.txt').read().splitlines()


class Particle:

    def __init__(self, input_line: str):
        m = pattern.match(input_line)
        self.params = {k: int(v) for k, v in m.groupdict().items()}

    def has_collision(self, other: Particle) -> bool:
        # Find coefficients for the quadratic equation describing the times that the 2 particles have the same x pos
        a = (self.params['ax'] - other.params['ax']) / 2
        b = a + self.params['vx'] - other.params['vx']
        c = self.params['px'] - other.params['px']

        # indicates an imaginary number
        if pow(b, 2) < 4 * a * c or a == 0:
            return False

        integer_roots: List[int] = []
        radical = math.sqrt(pow(b, 2) - 4 * a * c)
        v1 = (-b + radical) / (2 * a)
        if v1.is_integer():
            integer_roots.append(int(v1))

        v2 = (-b - radical) / (2 * a)
        if v2.is_integer():
            integer_roots.append(int(v2))

        for root in integer_roots:
            if self.x(root) == other.x(root) \
                    and self.y(root) == other.y(root) \
                    and self.z(root) == other.z(root):
                return True

        return False

    def x(self, root):
        return self.location('x', root)

    def y(self, root):
        return self.location('y', root)

    def z(self, root):
        return self.location('z', root)

    def location(self, axis: str, time: int) -> int:
        return self.params['p' + axis] + (self.params['v' + axis] * time) + \
               (self.params['a' + axis] * ((time * (time + 1)) / 2))


particles: List[Particle] = []

for p in particle_input:
    particles.append(Particle(p))

destroyed = set()
for (p1, p2) in itertools.combinations(particles, 2):
    if p1.has_collision(p2):
        destroyed.add(p1)
        destroyed.add(p2)

print(str(len(particles) - len(destroyed)))
