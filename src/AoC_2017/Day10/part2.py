# filename = "test1.txt"
# SIZE = 5
from src.AoC_2017.Day10.HashKnot import HashKnot

filename = "input.txt"

assert(HashKnot('').hash() == 'a2582a3a0e66e6e86e3812dcb672a272')
assert(HashKnot('AoC 2017').hash() == '33efeb34ea91902bb2f59c9920caa6cd')
assert(HashKnot('1,2,3').hash() == '3efbe78a8d82f29979031a4aa0b16a9d')
assert(HashKnot('1,2,4').hash() == '63960835bcdc130f0b66d7ff4f6a5a8e')
print(HashKnot(open(filename).read()).hash())
