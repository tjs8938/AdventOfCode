input_file = open("input.txt")
# input_file = open("test1.txt")
# input_file = open("test2.txt")

input_lines = input_file.read().splitlines()
adapters = [int(x) for x in input_lines]
adapters.sort()

diffs = {}

prev_adapter = 0
for a in adapters:
    diff = str(a - prev_adapter)
    if diff not in diffs:
        diffs[diff] = 0
    diffs[diff] += 1
    prev_adapter = a

print(diffs)
print(diffs['1'] * (diffs['3'] + 1))
