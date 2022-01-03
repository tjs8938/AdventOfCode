from src.AoC_2017.Day10.HashKnot import HashKnot

key = "jxqlasbh-"

on = 0
for i in range(128):
    k = key + str(i)
    knot = HashKnot(k).hash()
    dec = int(knot, 16)
    while dec > 0:
        on += 1
        dec = dec & (dec - 1)

print(on)
