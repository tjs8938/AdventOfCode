import re
from typing import Dict, List

filename = "input.txt"
# filename = "test1.txt"

file = open(filename)
input_lines = file.read().splitlines()


class Ingredient:

    def __init__(self, name: str, line: str):
        self.name = name
        self.properties = {}
        property_strings = line.split(', ')
        for string in property_strings:
            m = re.match("([a-z]*) (.*)", string)
            self.properties[m.group(1)] = int(m.group(2))

    def __hash__(self):
        return hash(self.name)


all_ingredients: List[Ingredient] = []
for line in input_lines:
    m = re.match("^(.*): (.*)", line)
    all_ingredients.append(Ingredient(m.group(1), m.group(2)))


class Cookie:

    def __init__(self):
        self.recipe: Dict[Ingredient, int] = {}

    def score(self):
        score = 1
        properties = {}
        for ingredient, measure in self.recipe.items():
            for prop_name, prop_value in ingredient.properties.items():
                if prop_name not in properties:
                    properties[prop_name] = 0
                properties[prop_name] += (measure * prop_value)

        for key, value in properties.items():
            if key != "calories":
                score *= (value if value > 0 else 0)

        return score


highest = 0

for i in range(101):
    for j in range(101 - i):
        for k in range(101 - i - j):
            # l = 100 - i
            l = 100 - (i + j + k)
            c = Cookie()
            c.recipe[all_ingredients[0]] = i
            c.recipe[all_ingredients[1]] = j
            c.recipe[all_ingredients[2]] = k
            c.recipe[all_ingredients[3]] = l
            # c.recipe[all_ingredients[1]] = l
            if c.score() > highest:
                highest = c.score()

print(highest)
