filename = "input.txt"
# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()

found = {}

for line in input_lines:
    key = str(2020 - int(line))
    if line in found:
        print("Found " + key + " and " + line + " which multiply to " + str(int(key) * int(line)))
        break
    else:
        found[key] = line


