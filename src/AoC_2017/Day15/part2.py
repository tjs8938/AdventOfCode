
def gen(start: int, factor: int, divisor: int) -> int:
    value = start
    while True:
        value *= factor
        value = (value & 0x7FFFFFFF) + (value >> 31)
        value = value if value < 0x7FFFFFFF else value - 0x7FFFFFFF
        if value & (divisor - 1) == 0:
            yield value


# test
# gen_a = gen(65, 16807, 4)
# gen_b = gen(8921, 48271, 8)
# real
gen_a = gen(618, 16807, 4)
gen_b = gen(814, 48271, 8)

count = 0
for i in range(5000000):
    if (gen_a.__next__() & 0xFFFF) == (gen_b.__next__() & 0xFFFF):
        count += 1

print(count)