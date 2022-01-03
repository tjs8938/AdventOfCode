import re
from typing import List

def_regex = re.compile(r'(.*),(.*)')


def print_matrix(data):
    for row in data:
        print(" ".join(row))


def dict_to_matrix(data, regex=def_regex, empty='.', xform=None):
    lowest_x = int(regex.match(min(data, key=lambda n: int(regex.match(n).group(1)))).group(1))
    lowest_y = int(regex.match(min(data, key=lambda n: int(regex.match(n).group(2)))).group(2))
    ret_val = []
    for key in data:
        m = regex.match(key)
        x = int(m.group(1)) - lowest_x
        y = int(m.group(2)) - lowest_y

        while len(ret_val) <= y:
            ret_val.append([])

        while len(ret_val[y]) <= x:
            ret_val[y].append(empty)

        ret_val[y][x] = data[key] if xform is None else xform(data[key])

    return ret_val


def tuple_dict_to_matrix(data, empty='.', xform=None):
    lowest_x = min(data, key=lambda n: n[0])[0]
    lowest_y = min(data, key=lambda n: n[1])[1]
    ret_val: List[List[str]] = []
    for key in data:
        x = key[0] - lowest_x
        y = key[1] - lowest_y

        while len(ret_val) <= y:
            ret_val.append([])

        while len(ret_val[y]) <= x:
            ret_val[y].append(empty)

        ret_val[y][x] = data[key] if xform is None else xform(data[key])

    return ret_val


def pair_to_key(x):
    return str(x[0]) + ',' + str(x[1])


def position_to_key(x, y):
    return str(x) + ',' + str(y)


def flip_vertical(matrix):
    flipped = []
    for i in range(len(matrix), 0, -1):
        flipped.append(matrix[i - 1])
    return flipped


def flip_horizontal(matrix):
    flipped = []
    for i in range(len(matrix)):
        flipped.append(matrix[i][::-1])
    return flipped


def rotate_left(matrix):
    spun = []
    for x in range(len(matrix), 0, -1):
        s = ""
        for y in range(len(matrix)):
            s += matrix[y][x - 1]
        spun.append(s)
    return spun


def rotate_right(matrix):
    spun = []
    for x in range(len(matrix)):
        s = ""
        for y in range(len(matrix), 0, -1):
            s += matrix[y - 1][x]
        spun.append(s)
    return spun
