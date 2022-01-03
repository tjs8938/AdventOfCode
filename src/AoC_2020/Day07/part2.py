import re

filename = "input.txt"
# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()

first_bag = re.compile("^(.*) bags contain (.*)")
included_bags = re.compile("([0-9]+) ([^0-9,]*) bag")


class Bag:

    def __init__(self, color):
        self.color = color
        self.children = []
        self.parents = []

    def add_child(self, child):
        self.children.append(child)
        child[1].parents.append(self)

    def contains_x_bags(self):
        bag_count = 0
        for pair in self.children:
            bag_count += pair[0] * (pair[1].contains_x_bags() + 1)
        return bag_count


all_bags = {}


def get_bag(color):
    if color not in all_bags:
        b = Bag(color)
        all_bags[color] = b

    return all_bags[color]


for line in input_lines:
    m = first_bag.match(line)
    parent = get_bag(m.group(1))

    child_name_list = included_bags.findall(m.group(2))
    for pair in child_name_list:
        parent.add_child((int(pair[0]), get_bag(pair[1])))

print(all_bags['shiny gold'].contains_x_bags())
