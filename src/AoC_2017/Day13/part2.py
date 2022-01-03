from typing import List, Tuple


def find_delay(filename: str) -> int:

    firewall: List[Tuple[int, int]] = [(int(x[0]), int(x[1])) for x in map(lambda line: line.split(': '), open(filename).read().splitlines())]
    delay = 1

    while True:
        collision = False
        for index in range(0, len(firewall)):
            layer = firewall[index]
            if (layer[0] + delay) % ((layer[1] - 1) * 2) == 0:
                collision = True
                break

        if collision:
            delay += 1
            continue

        return delay


assert(find_delay('test1.txt') == 10)
print(find_delay('input.txt'))
