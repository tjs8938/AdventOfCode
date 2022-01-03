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
group_count = 0


def clean_answers():
    global answers
    new_answers = answers.copy()
    for k, v in new_answers.items():
        if v < group_count:
            del answers[k]
    groups.append(answers)


for line in input_lines:
    if len(line) == 0:
        clean_answers()
        answers = {}
        group_count = 0
    else:
        group_count += 1
        for c in line:
            if c not in answers:
                answers[c] = 0
            answers[c] += 1

clean_answers()

total = 0
for g in groups:
    print(g)
    total += len(g)

print(groups)
print(total)
