import re

filename = "input.txt"

file = open(filename)
input_lines = file.read().splitlines()


real_sue = {"children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1}


class AuntSue:

    def __init__(self, number: int, properties: str):
        self.number = number
        self.props = {}
        for p in re.findall("([a-z]+): ([0-9]+)", properties):
            self.props[p[0]] = int(p[1])


for line in input_lines:
    m = re.match("Sue ([0-9]*): (.*)", line)
    sue = AuntSue(int(m.group(1)), m.group(2))
    good_sue = True
    for p, v in sue.props.items():
        if p in ["cats", "trees"]:
            if v <= real_sue[p]:
                good_sue = False
                break
        elif p in ["pomeranians", "goldfish"]:
            if v >= real_sue[p]:
                good_sue = False
                break
        else:
            if v != real_sue[p]:
                good_sue = False
                break

    if good_sue:
        print(sue.number)
