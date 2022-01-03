
a = 1
b = 0

a *= 3
a += 1
a += 1
a *= 3
a += 1
a += 1
a *= 3
a *= 3
a += 1
a += 1
a *= 3
a += 1
a *= 3
a += 1
a *= 3
a += 1
a += 1
a *= 3
a += 1
a *= 3
a *= 3
a += 1

while a != 1:
    b += 1
    if a % 2 == 1:
        a *= 3
        a += 1
    else:
        a = a >> 1

print(b)