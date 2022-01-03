import re
import string

filename = "input.txt"

# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()

find_escapes_and_quotes = re.compile("([\"\\\\])")

diff = 0

for line in input_lines:
    diff += len(find_escapes_and_quotes.findall(line)) + 2

print(diff)
