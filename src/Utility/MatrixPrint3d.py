import itertools
import re
from typing import List

def_regex = re.compile(r'(.*),(.*),(.*)')


def dict_to_matrix(data, regex=def_regex, empty='.', xform=None):
    lowest_x = key_to_position(min(data, key=lambda n: key_to_position(n, regex)[0]), regex)[0]
    lowest_y = key_to_position(min(data, key=lambda n: key_to_position(n, regex)[1]), regex)[1]
    lowest_z = key_to_position(min(data, key=lambda n: key_to_position(n, regex)[2]), regex)[2]
    ret_val = []
    for key in data:
        m = regex.match(key)
        x = int(m.group(1)) - lowest_x
        y = int(m.group(2)) - lowest_y
        z = int(m.group(3)) - lowest_z

        while len(ret_val) <= z:
            ret_val.append([])

        while len(ret_val[z]) <= y:
            ret_val[z].append([])

        while len(ret_val[z][y]) <= x:
            ret_val[z][y].append(empty)

        ret_val[z][y][x] = data[key] if xform is None else xform(data[key])

    for i in range(len(ret_val)):
        print("z=" + str(i + lowest_z))
        plane = ret_val[i]
        for row in plane:
            print(" ".join(row))


def key_to_position(key, regex):
    x = int(regex.match(key).group(1))
    y = int(regex.match(key).group(2))
    z = int(regex.match(key).group(3))
    return x, y, z


def pair_to_key(x):
    return str(x[0]) + ',' + str(x[1]) + ',' + str(x[2])


def position_to_key(x, y, z):
    return str(x) + ',' + str(y) + ',' + str(z)


def find_neighboring_positions(pos: str, regex=def_regex) -> List[str]:
    x, y, z = key_to_position(pos, regex)
    offsets = [-1, 0, 1]
    offset_combos = itertools.product(offsets, repeat=3)
    neighboring_positions = []
    for combo in offset_combos:
        if combo[0] != 0 or combo[1] != 0 or combo[2] != 0:
            px = x + combo[0]
            py = y + combo[1]
            pz = z + combo[2]
            neighboring_positions.append(position_to_key(px, py, pz))

    return neighboring_positions
