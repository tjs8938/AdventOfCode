
values_seen = set()
last_value = 0

a = 0
while True:
    b = a | 65536
    a = 10605201
    while b > 0:
        c = b & 255
        a += c
        a = a & 16777215
        a *= 65899
        a = a & 16777215
        b = b // 256
    if a not in values_seen:
        values_seen.add(a)
        last_value = a
    else:
        print(last_value)
        break
