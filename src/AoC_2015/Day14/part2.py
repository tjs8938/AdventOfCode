import re

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

        self.total_traveled = 0
        self.time_passed = 0
        self.points = 0

    def tick(self):
        if self.time_passed % (self.duration + self.rest) < self.duration:
            self.total_traveled += self.velocity
        self.time_passed += 1

    def score(self, furthest):
        if self.total_traveled == furthest:
            self.points += 1


reindeer = {}

for line in input_lines:
    m = pattern.match(line)
    name = m.group(1)
    reindeer[name] = Deer(int(m.group(2)), int(m.group(3)), int(m.group(4)))

for i in range(time):
    for deer in reindeer.values():
        deer.tick()

    furthest_traveled = max(map(lambda x: x.total_traveled, reindeer.values()))

    for deer in reindeer.values():
        deer.score(furthest_traveled)

print(max(map(lambda x: x.points, reindeer.values())))
