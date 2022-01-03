import hashlib

prefix = "ckczppom"
suffix = 1

while True:
    key = prefix + str(suffix)
    result = hashlib.md5(key.encode())
    if result.hexdigest().startswith("00000"):
        print(suffix)
        break

    suffix += 1