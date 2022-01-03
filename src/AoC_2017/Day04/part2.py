
import itertools

# filename = "test1.txt"
filename = "input.txt"


input_lines = open(filename).read().splitlines()
count = 0


for line in input_lines:
    words = line.split()
    if len(words) == len(set(words)):
        found_conflict = False

        for pair in itertools.combinations(words, 2):
            if set(pair[0]) == set(pair[1]):
                found_mismatch = False
                for l in pair[0]:
                    if pair[0].count(l) != pair[1].count(l):
                        found_mismatch = True
                        break

                if not found_mismatch:
                    found_conflict = True
                    break

        if not found_conflict:
            count += 1

print(count)
