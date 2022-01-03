import re
from functools import cmp_to_key

# inputs = open("test1.txt").read().splitlines()
inputs = open("input.txt").read().splitlines()

letter_counts = []
for i in range(len(inputs[0])):
    letter_counts.append({})

for line in inputs:
    for i in range(len(line)):
        letter_counts[i].setdefault(line[i], 0)
        letter_counts[i][line[i]] += 1

print(letter_counts)


message = ""
for pos in range(len(letter_counts)):
    best_count = 0
    best_letter = None
    for letter, count in letter_counts[pos].items():
        if count > best_count:
            best_letter = letter
            best_count = count
    message += best_letter

print(message)
