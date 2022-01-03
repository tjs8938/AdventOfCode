import hashlib
from typing import Dict, Tuple, List

# salt = "abc"  # Test
salt = "ihaygndm"  # Real
index = 0

candidates: Dict[str, List[Tuple[str, int]]] = {}
keys: List[Tuple[str, int]] = []

list_hashes = []


def look_for_string(string, index):
    for i in range(index, index + 1000):
        h: str = get_md5(i)
        if h.find(string) >= 0:
            return True
    return False


def get_md5(i):
    index = i
    while len(list_hashes) <= i:
        list_hashes.append(hashlib.md5((salt + str(index)).encode()).hexdigest())
        index += 1
    return list_hashes[i]


while len(keys) < 64:
    key = salt + str(index)
    result: str = get_md5(index)

    char_count = 0
    for c in range(len(result)):
        if c == 0 or result[c] != result[c - 1]:
            char_count = 1
        else:
            char_count += 1

        if char_count == 3:
            if look_for_string(result[c] * 5, index+1):
                keys.append((result, index))
            break
    index += 1

print(keys[-1][1])
