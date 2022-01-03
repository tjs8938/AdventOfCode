import functools
import itertools

filename = "input.txt"
# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()

found = {}

for tup in itertools.product(input_lines, input_lines, input_lines):
    if functools.reduce(lambda a, b: int(a) + int(b), tup) == 2020:
        print("Found " + str(tup))
        break
