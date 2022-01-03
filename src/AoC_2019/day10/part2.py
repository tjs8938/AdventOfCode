import math


class Asteroid:
    def __init__(self, location):
        self.location = location
        self.visible = {}

    def __getitem__(self, item):
        return self.location.__getitem__(item)


file = open('input.txt')

# file = open('test1.txt')  # Best is 5,8 with 33 other asteroids detected
# file = open('test2.txt')  # Best is 1,2 with 35 other asteroids detected
# file = open('test3.txt')  # Best is 6,3 with 41 other asteroids detected
# file = open('test4.txt')  # Best is 11,13 with 210 other asteroids detected

asteroid_field = file.read().splitlines()
# for item in product(range(0, 25), range(0, 25)):
#     print(item)
# print(list(filter(lambda x: math.gcd(x[0], x[1]) == 1, product(range(0, 25), range(0, 25)))))

asteroids = list()

for x in range(0, len(asteroid_field[0])):
    for y in range(0, len(asteroid_field)):
        if asteroid_field[y][x] == '#':
            new_asteroid = Asteroid((x, y))

            for asteroid in reversed(asteroids):
                slope = (asteroid[1] - new_asteroid[1], asteroid[0] - new_asteroid[0])
                gcd = math.gcd(slope[0], slope[1])

                slope = (slope[1] / gcd, slope[0] / gcd)
                sign = "-" if ((slope[0] < 0) != (slope[1] < 0)) else '+'

                key = sign + str(abs(slope[1])) + "/" + str(abs(slope[0]))
                if (key + "<") not in new_asteroid.visible:
                    new_asteroid.visible[key + "<"] = asteroid
                    asteroid.visible[key + ">"] = new_asteroid

            asteroids.append(new_asteroid)

asteroids.sort(key=lambda n: len(n.visible))

station = asteroids[-1]

print(station.location, len(station.visible))

others = list(station.visible.values())
others.sort(key=lambda n: 180 - math.degrees(math.atan2(station[1] - n[1], station[0] - n[0]))
if 180 - math.degrees(math.atan2(station[1] - n[1], station[0] - n[0])) <= 90
else 180 - math.degrees(math.atan2(station[1] - n[1], station[0] - n[0])) - 360, reverse=True)

for a in others:
    # tan = math.tan()
    print(a.location, 180 - math.degrees(math.atan2(station[1] - a.location[1], station[0] - a.location[0])))

print(others[199].location)
