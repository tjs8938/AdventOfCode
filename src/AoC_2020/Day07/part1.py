import re

filename = "input.txt"
# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()

first_bag = re.compile("^(.*) bags contain (.*)")
included_bags = re.compile("([0-9]*) ([^0-9,]*) bag")


class Bag:

    def __init__(self, color):
        self.color = color
        self.children = []
        self.parents = []

    def add_child(self, child):
        self.children.append(child)
        child.parents.append(self)


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
        parent.add_child(get_bag(pair[1]))

containing_bags = set()


def process_bag(bag):
    for p in bag.parents:
        containing_bags.add(p.color)
        process_bag(p)


process_bag(all_bags['shiny gold'])
print(len(containing_bags))
