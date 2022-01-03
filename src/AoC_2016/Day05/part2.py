import hashlib
from functools import reduce

prefix = "ffykfhsq"
suffix = 0

door_id = ["0", "1", "2", "3", "4", "5", "6", "7"]
found = 0

while found < 255:
    key = prefix + str(suffix)
    result = hashlib.md5(key.encode())
    if result.hexdigest().startswith("00000"):
        position = result.hexdigest()[5]
        if position in ["0", "1", "2", "3", "4", "5", "6", "7"] and found & (1 << int(position)) == 0:
            door_id[int(position)] = result.hexdigest()[6]
            found = found | (1 << int(position))
            print("Inserting " + result.hexdigest()[6] + " at position " + position)

    suffix += 1

print(reduce(lambda a, b: a + b, list(door_id)))

# ac35d825