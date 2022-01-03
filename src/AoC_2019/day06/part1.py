
input_file = open("input.txt")
input = input_file.read().splitlines()


class Planet:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.orbits = None

    def set_parent(self, parent):
        self.parent = parent

    def get_orbits(self):
        if self.orbits is not None:
            return self.orbits
        elif self.parent is None:
            return 0
        else:
            self.orbits = self.parent.get_orbits()+1
            return self.orbits


planet_map = {}

for line in input:
    parent = line[0:line.index(')')]
    child = line[line.index(')')+1:]

    parent_node = planet_map[parent] if parent in planet_map else Planet(parent)
    child_node = planet_map[child] if child in planet_map else Planet(child)
    print(parent_node)
    print(child_node)
    child_node.set_parent(parent_node)

    planet_map[parent] = parent_node
    planet_map[child] = child_node

print(planet_map)

total_orbits = 0
for planet in planet_map:
    total_orbits += planet_map[planet].get_orbits()

print(total_orbits)
