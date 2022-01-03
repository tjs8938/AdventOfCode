import itertools
import re
from typing import List

def_regex = re.compile(r'(.*),(.*),(.*),(.*)')


def dict_to_matrix(data, regex=def_regex, empty='.', xform=None):
    lowest_x = key_to_position(min(data, key=lambda n: key_to_position(n, regex)[0]), regex)[0]
    lowest_y = key_to_position(min(data, key=lambda n: key_to_position(n, regex)[1]), regex)[1]
    lowest_z = key_to_position(min(data, key=lambda n: key_to_position(n, regex)[2]), regex)[2]
    lowest_w = key_to_position(min(data, key=lambda n: key_to_position(n, regex)[3]), regex)[3]
    ret_val = []
    for key in data:
        m = regex.match(key)
        x = int(m.group(1)) - lowest_x
        y = int(m.group(2)) - lowest_y
        z = int(m.group(3)) - lowest_z
        w = int(m.group(4)) - lowest_w

        while len(ret_val) <= w:
            ret_val.append([])

        while len(ret_val[w]) <= z:
            ret_val[w].append([])

        while len(ret_val[w][z]) <= y:
            ret_val[w][z].append([])

        while len(ret_val[w][z][y]) <= x:
            ret_val[w][z][y].append(empty)

        ret_val[w][z][y][x] = data[key] if xform is None else xform(data[key])

    for j in range(len(ret_val)):
        for i in range(len(ret_val[j])):
            print("z=" + str(i + lowest_z) + ", w=" + str(j + lowest_w))
            plane = ret_val[j][i]
            for row in plane:
                print(" ".join(row))


def key_to_position(key, regex):
    x = int(regex.match(key).group(1))
    y = int(regex.match(key).group(2))
    z = int(regex.match(key).group(3))
    w = int(regex.match(key).group(4))
    return x, y, z, w


def pair_to_key(x):
    return str(x[0]) + ',' + str(x[1]) + ',' + str(x[2]) + ',' + str(x[3])


def position_to_key(x, y, z, w):
    return str(x) + ',' + str(y) + ',' + str(z) + ',' + str(w)


def find_neighboring_positions(pos: str, regex=def_regex) -> List[str]:
    x, y, z, w = key_to_position(pos, regex)
    offsets = [-1, 0, 1]
    offset_combos = itertools.product(offsets, repeat=4)
    neighboring_positions = []
    for combo in offset_combos:
        if combo[0] != 0 or combo[1] != 0 or combo[2] != 0 or combo[3] != 0:
            px = x + combo[0]
            py = y + combo[1]
            pz = z + combo[2]
            pw = w + combo[3]
            neighboring_positions.append(position_to_key(px, py, pz, pw))

    return neighboring_positions
