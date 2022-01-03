import re

rule_pattern = re.compile("^([0-9]*): (.*)$")

input_file = open("input.txt")
rules_file = open("rules.txt")
# input_file = open("test_input.txt")
# rules_file = open("test_rules.txt")
# input_file = open("test1.txt")
input_lines = input_file.read().splitlines()
rules_lines = rules_file.read().splitlines()

rules = {}


def parse_piece(param):
    split_rules = param.split()
    return "".join([rules[x].get_regex() for x in split_rules])


class Rule:

    def __init__(self, string):
        self.regex = None
        self.str_rep = string

    def get_regex(self):
        if self.regex is None:
            rule_pieces = self.str_rep.split('|')
            if len(rule_pieces) == 1:
                self.regex = parse_piece(rule_pieces[0])
            else:
                self.regex = '(' + '|'.join([parse_piece(x) for x in rule_pieces]) + ')'
        return self.regex


rule_a = Rule("a")
rule_a.regex = 'a'
rule_b = Rule("b")
rule_b.regex = 'b'

# real
rules["106"] = rule_a
rules["29"] = rule_b

# test
# rules["4"] = rule_a
# rules["5"] = rule_b

for l in rules_lines:
    m = rule_pattern.match(l)
    rules[m.group(1)] = Rule(m.group(2))

print(rules["0"].get_regex())
print(rules["42"].get_regex())
print(rules["31"].get_regex())

count = 0
for l in input_lines:
    pattern = re.compile("^" + rules["0"].get_regex() + "$")
    if pattern.match(l):
        count += 1

print(count)
