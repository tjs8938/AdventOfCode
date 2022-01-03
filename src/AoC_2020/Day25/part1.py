
# Test
# card = 5764801
# door = 17807724
#
card = 13316116
door = 13651422

counter = 1
value = 7
while value != card:
    counter += 1
    value = value * 7 % 20201227


key = pow(door, counter) % 20201227
print(key)

