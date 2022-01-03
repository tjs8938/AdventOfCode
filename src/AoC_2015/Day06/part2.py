import re

lights = []
for x in range(1000):
    lights.append([])
    for y in range(1000):
        lights[x].append(0)

filename = "input.txt"
# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()

for line in input_lines:

    m = re.match(".*(on|off|toggle) ([0-9]*),([0-9]*) through ([0-9]*),([0-9]*)", line)
    op = m.group(1)
    x1 = int(m.group(2))
    y1 = int(m.group(3))
    x2 = int(m.group(4))
    y2 = int(m.group(5))

    for v in range(y1, y2+1):
        for h in range(x1, x2+1):
            if op == 'on':
                lights[v][h] += 1
            elif op == 'off':
                lights[v][h] = 0 if lights[v][h] == 0 else lights[v][h] - 1
            else:
                lights[v][h] += 2

brightness = 0
for row in lights:
    for col in row:
        brightness += col

print(brightness)

