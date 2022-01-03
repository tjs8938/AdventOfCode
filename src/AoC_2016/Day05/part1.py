import hashlib

prefix = "ffykfhsq"
suffix = 0

door_id = ""

while len(door_id) < 8:
    key = prefix + str(suffix)
    result = hashlib.md5(key.encode())
    if result.hexdigest().startswith("00000"):
        door_id += result.hexdigest()[5]

    suffix += 1

print(door_id)
