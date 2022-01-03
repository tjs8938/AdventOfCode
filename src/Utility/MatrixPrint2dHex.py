import re
from typing import List

def_regex = re.compile(r'(.*),(.*)')

MOVES = {'sw': lambda x: (x[0], x[1] - 1),
         'w': lambda x: (x[0] - 1, x[1]),
         'ne': lambda x: (x[0], x[1] + 1),
         'e': lambda x: (x[0] + 1, x[1]),
         'nw': lambda x: (x[0] - 1, x[1] + 1),
         'se': lambda x: (x[0] + 1, x[1] - 1)
         }


def dict_to_matrix(data, regex=def_regex, empty='.', xform=None):
    lowest_x = key_to_position(min(data, key=lambda n: key_to_position(n, regex)[0]), regex)[0]
    lowest_y = key_to_position(min(data, key=lambda n: key_to_position(n, regex)[1]), regex)[1]
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

    for row in ret_val:
        print(" ".join(row))


def key_to_position(key, regex):
    x = int(regex.match(key).group(1))
    y = int(regex.match(key).group(2))
    return x, y


def pair_to_key(x):
    return str(x[0]) + ',' + str(x[1])


def position_to_key(x, y):
    return str(x) + ',' + str(y)


def find_neighboring_positions(pos: str, regex=def_regex) -> List[str]:
    position = (key_to_position(pos, regex))
    neighboring_positions = []
    for d in MOVES.values():
        neighboring_positions.append(pair_to_key(d(position)))

    return neighboring_positions

