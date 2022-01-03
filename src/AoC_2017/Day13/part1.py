from typing import List, Tuple


def sev(filename: str) -> int:

    firewall: List[Tuple[int, int]] = [(int(x[0]), int(x[1])) for x in map(lambda line: line.split(': '), open(filename).read().splitlines())]
    severity = 0
    for index in range(1, len(firewall)):
        layer = firewall[index]
        if layer[0] % ((layer[1] - 1) * 2) == 0:
            severity += layer[0] * layer[1]

    return severity


assert(sev('test1.txt') == 24)
print(sev('input.txt'))