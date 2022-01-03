import re

filename = "input.txt"
# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()

groups = []
answers = {}

for line in input_lines:
    if len(line) == 0:
        groups.append(answers)
        answers = {}
    else:
        for c in line:
            if c not in answers:
                answers[c] = 0
            answers[c] += 1
groups.append(answers)

total = 0
for g in groups:
    print(g)
    total += len(g)

print(groups)
print(total)
