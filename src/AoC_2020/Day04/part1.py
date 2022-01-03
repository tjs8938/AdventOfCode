import re

filename = "input.txt"
# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()

fields = re.compile("(byr|iyr|eyr|hgt|hcl|ecl|pid):")

buffer = ""
valid_count = 0

for line in input_lines:
    if len(line) > 0:
        buffer = buffer + " " + line
    else:
        # print(buffer, len(fields.findall(buffer)))
        if len(fields.findall(buffer)) == 7:
            valid_count += 1
        buffer = ""


print(buffer)
print(valid_count)
