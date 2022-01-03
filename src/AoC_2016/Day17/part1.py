import hashlib
from typing import List, Tuple, Callable

strategies: List[Tuple[str, Callable]] = [
    ('U', lambda x: (x[0], x[1] - 1)),
    ('D', lambda x: (x[0], x[1] + 1)),
    ('L', lambda x: (x[0] - 1, x[1])),
    ('R', lambda x: (x[0] + 1, x[1]))
]


def shortest_path(passcode: str) -> str:
    paths_to_process: List[Tuple[str, Tuple[int, int]]] = [("", (0, 0))]

    while len(paths_to_process) > 0:
        path = paths_to_process.pop(0)
        hashcode = hashlib.md5((passcode + path[0]).encode()).hexdigest()
        for direction in range(4):
            if hashcode[direction] in ['b', 'c', 'd', 'e', 'f']:
                strategy = strategies[direction]
                new_pos = strategy[1](path[1])
                if new_pos[0] == 3 and new_pos[1] == 3:
                    return path[0] + strategy[0]
                elif 0 <= new_pos[0] < 4 and 0 <= new_pos[1] < 4:
                    paths_to_process.append((path[0] + strategy[0], new_pos))


assert (shortest_path("ihgpwlah") == "DDRRRD")
assert (shortest_path("kglvqrro") == "DDUDRLRRUDRD")
assert (shortest_path("ulqzkmiv") == "DRURDRUDDLLDLUURRDULRLDUUDDDRR")
print(shortest_path("rrrbmfta"))


def longest_path(passcode: str) -> int:
    paths_to_process: List[Tuple[str, Tuple[int, int]]] = [("", (0, 0))]
    paths_to_end: List[str] = []

    while len(paths_to_process) > 0:
        path = paths_to_process.pop(0)
        hashcode = hashlib.md5((passcode + path[0]).encode()).hexdigest()
        for direction in range(4):
            if hashcode[direction] in ['b', 'c', 'd', 'e', 'f']:
                strategy = strategies[direction]
                new_pos = strategy[1](path[1])
                if new_pos[0] == 3 and new_pos[1] == 3:
                    paths_to_end.append(path[0] + strategy[0])
                elif 0 <= new_pos[0] < 4 and 0 <= new_pos[1] < 4:
                    paths_to_process.append((path[0] + strategy[0], new_pos))

    longest = 0
    for path in paths_to_end:
        if len(path) > longest:
            longest = len(path)
    return longest


assert (longest_path("ihgpwlah") == 370)
assert (longest_path("kglvqrro") == 492)
assert (longest_path("ulqzkmiv") == 830)
print(longest_path("rrrbmfta"))