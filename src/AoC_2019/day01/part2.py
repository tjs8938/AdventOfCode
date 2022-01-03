import math

input_file = open("input.txt")
input = input_file.read().splitlines()


def calc_fuel(mass):
    f = math.floor(mass/3)-2

    if f <= 0:
        return 0

    return f + calc_fuel(f)


fuel_required = 0

for line in input:
    fuel_required += calc_fuel(int(line))
# fuel_required = calc_fuel(100756)

print(fuel_required)
