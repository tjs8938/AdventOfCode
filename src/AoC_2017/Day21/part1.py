import re
from functools import reduce

from src.Utility.MatrixPrint import rotate_left, flip_horizontal, print_matrix

# filename = "test1.txt"
# steps = 2

filename = "input.txt"
steps = 18

pattern = re.compile("(.*) => (.*)")

picture = ['.#.',
           '..#',
           '###']

rules = {}

for line in open(filename).read().splitlines():
    m = pattern.match(line)
    key = m.group(1)
    value = m.group(2)

    key_matrix = key.split('/')
    for i in range(4):
        key_matrix = rotate_left(key_matrix)
        rules[reduce(lambda a, b: a + '/' + b, key_matrix)] = value

        key_matrix = flip_horizontal(key_matrix)
        rules[reduce(lambda a, b: a + '/' + b, key_matrix)] = value
        key_matrix = flip_horizontal(key_matrix)

print(len(rules))
print(rules)

for step in range(steps):

    if len(picture) % 2 == 0:
        split_size = 2
    else:
        split_size = 3

    new_rows = int(((split_size + 1) * len(picture)) / split_size)
    new_picture = ['' for x in range(new_rows)]

    for big_row in range(int(len(picture) / split_size)):

        for big_col in range(int(len(picture) / split_size)):

            key_matrix = [row[big_col * split_size:(big_col * split_size) + split_size]
                          for row in picture[big_row * split_size:(big_row * split_size) + split_size]]
            key = reduce(lambda a, b: a + '/' + b, key_matrix)
            replacement = rules[key]

            for row_index, string in \
                    zip(range(big_row * (split_size + 1), (big_row * (split_size + 1)) + split_size + 1),
                        replacement.split('/')):
                new_picture[row_index] += string

    picture = new_picture
    # print(picture)

    count = 0
    for row in picture:
        count += row.count('#')
    # print_matrix(picture)

    print(step, count)
