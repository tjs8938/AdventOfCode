
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

    def get_path(self):
        if self.parent is None:
            path = [self.name]
            return path
        else:
            path = self.parent.get_path()
            path.append(self.name)
            return path

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


planet_map = {}

for line in input:
    parent = line[0:line.index(')')]
    child = line[line.index(')')+1:]

    parent_node = planet_map[parent] if parent in planet_map else Planet(parent)
    child_node = planet_map[child] if child in planet_map else Planet(child)

    child_node.set_parent(parent_node)

    planet_map[parent] = parent_node
    planet_map[child] = child_node


my_path = planet_map["YOU"].parent.get_path()
santa_path = planet_map["SAN"].parent.get_path()

print(my_path)
print(santa_path)

common_parent = 'COM'
for planet in santa_path:
    if planet in my_path:
        common_parent = planet

print(common_parent)
print(len(my_path[my_path.index(common_parent)+1:]) + len(santa_path[santa_path.index(common_parent)+1:]))
