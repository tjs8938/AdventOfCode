import re


def distinct_molecules(starting_molecule: str, filename: str) -> int:
    input_lines = open(filename).read().splitlines()

    rules = {}
    for line in input_lines:
        m = re.match("(.*) => (.*)", line)
        if m.group(1) not in rules:
            rules[m.group(1)] = set()
        rules[m.group(1)].add(m.group(2))

    rule_regex = re.compile("(" + "|".join(rules.keys()) + ")")
    index = 0
    new_molecules = set()
    match = rule_regex.search(starting_molecule, index)
    while match is not None:
        for rule in rules[match.group(1)]:
            new_molecules.add(starting_molecule[:match.start()] + rule + starting_molecule[match.end():])
        index = match.end()
        match = rule_regex.search(starting_molecule, index)

    # print(rules)
    # print(re.findall(rule_regex, starting_molecule))
    # print(new_molecules)
    return len(new_molecules)


assert (distinct_molecules("HOH", "test1.txt") == 4)
assert (distinct_molecules("HOHOHO", "test1.txt") == 7)
print(distinct_molecules(
    "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl",
    "input.txt"))
