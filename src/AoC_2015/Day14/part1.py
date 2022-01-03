import re
from math import floor

filename = "input.txt"
time = 2503
# filename = "test1.txt"
# time = 1000

file = open(filename)
input_lines = file.read().splitlines()
pattern = re.compile("(.*) can fly ([0-9]*) km/s for ([0-9]*) seconds, but then must rest for ([0-9]*) seconds.")


class Deer:

    def __init__(self, velocity, duration, rest):
        self.duration = duration
        self.velocity = velocity
        self.rest = rest

    def distance(self, time):
        full_iterations = floor(time / (self.duration + self.rest))
        full_iter_time = full_iterations * (self.duration + self.rest)
        return self.velocity * ((self.duration * full_iterations) + min(self.duration, time - full_iter_time))


reindeer = {}
distance = {}

for line in input_lines:
    m = pattern.match(line)
    name = m.group(1)
    reindeer[name] = Deer(int(m.group(2)), int(m.group(3)), int(m.group(4)))

    distance[name] = reindeer[name].distance(time)

print(distance)