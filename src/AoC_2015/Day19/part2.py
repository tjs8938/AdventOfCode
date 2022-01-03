import re
from typing import List, Set, Dict


def distinct_molecules(starting_molecule: str, rules: Dict[str, Set[str]]) -> Set[str]:
    rule_regex = re.compile("(" + "|".join(rules.keys()) + ")")
    index = 0
    new_molecules = set()
    match = rule_regex.search(starting_molecule, index)
    while match is not None:
        for rule in rules[match.group(1)]:
            new_molecules.add(starting_molecule[:match.start()] + rule + starting_molecule[match.end():])
        index = match.end()
        match = rule_regex.search(starting_molecule, index)

    return new_molecules


def build_rules(filename):
    input_lines = open(filename).read().splitlines()
    rules = {}
    for line in input_lines:
        m = re.match("(.*) => (.*)", line)
        if m.group(1) not in rules:
            rules[m.group(1)] = set()
        rules[m.group(1)].add(m.group(2))
    return rules


def build_reverse_rules(filename: str) -> Dict[str, str]:
    input_lines = open(filename).read().splitlines()
    rules = {}
    for line in input_lines:
        m = re.match("(.*) => (.*)", line)
        rules[m.group(2)] = m.group(1)
    return rules


def count_distinct_molecules(starting_molecule: str, filename: str) -> int:
    rules = build_rules(filename)
    return len(distinct_molecules(starting_molecule, rules))


def steps_to_molecule(starting_molecule: str, filename: str) -> int:
    rules = build_rules(filename)
    found_molecules = {'e': 0}
    current_set = set()
    current_set.add('e')
    steps = 1
    while starting_molecule not in found_molecules:
        temp_set = set()
        for molecule in current_set:
            new_molecules = distinct_molecules(molecule, rules)
            for m in new_molecules:
                if m not in found_molecules and len(m) <= len(starting_molecule):
                    found_molecules[m] = steps
                    temp_set.add(m)

        current_set = temp_set
        steps += 1

    return found_molecules[starting_molecule]


def source_molecules(molecule: str, rules: Dict[str, str]) -> List[str]:
    sources: List[str] = []
    for rule, replacement in rules.items():
        if replacement == 'e':
            if molecule == rule:
                return ['e']
        else:
            for index in range(len(molecule)):
                if molecule[index:].startswith(rule):
                    new_molecule = molecule[:index] + replacement + molecule[index + len(rule):]
                    sources.append(new_molecule)

    return sources


def steps_from_molecule(starting_molecule: str, filename: str) -> int:
    rules = build_reverse_rules(filename)
    found_molecules = {starting_molecule: 0}
    current_set = set()
    current_set.add(starting_molecule)
    steps = 1
    while 'e' not in found_molecules:
        temp_set = set()
        for molecule in current_set:
            new_molecules = source_molecules(molecule, rules)
            if new_molecules[0] == 'e':
                return steps
            else:
                for m in new_molecules:
                    if m not in found_molecules:
                        found_molecules[m] = steps
                        temp_set.add(m)

        current_set = temp_set
        steps += 1

    return found_molecules['e']


assert (count_distinct_molecules("HOH", "test1.txt") == 4)
assert (count_distinct_molecules("HOHOHO", "test1.txt") == 7)
print("Part 1: " + str(count_distinct_molecules(
    "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl",
    "input.txt")))


assert (steps_from_molecule("HOH", "test2.txt") == 3)
assert (steps_from_molecule("HOHOHO", "test2.txt") == 6)
print("Part 2: " + str(steps_from_molecule(
    "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl",
    "input.txt")))

