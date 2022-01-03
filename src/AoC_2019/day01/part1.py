import math

input_file = open("input.txt")
input = input_file.read().splitlines()

def calc_fuel(mass):
    return math.floor(mass/3)-2


sum = 0

for line in input:
    sum += calc_fuel(int(line))

print(sum)