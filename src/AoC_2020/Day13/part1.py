import re

time = 1002576
input_str = "13,x,x,x,x,x,x,37,x,x,x,x,x,449,x,29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,23,x,x,x,x,x,x,x,773,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17"

buses = [int(x) for x in re.findall("([0-9]+)", input_str)]

best_time = 99999999999999999999999999999999999
best_bus = -1

for bus in buses:
    bus_time = (time * -1) % bus
    if bus_time < best_time:
        best_time = bus_time
        best_bus = bus

print(best_bus * best_time)
