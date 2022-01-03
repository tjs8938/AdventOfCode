filename = "input.txt"
# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()

floor = 0
for c in input_lines[0]:
    if c == '(':
        floor += 1
    else:
        floor -= 1

print(floor)