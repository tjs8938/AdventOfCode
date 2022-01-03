from collections import defaultdict
from itertools import count

with open('input.txt') as file:
    input = file.read()

maze = defaultdict(lambda: ' ')
B, R = 0, 0
for y, row in enumerate(input.split('\n')):
    for x, c in enumerate(row):
        maze[x, y] = c
        R = max(R, x)
        B = max(B, y)

IL, IT, IR, IB = R, B, 0, 0
for y in range(2, B - 1):
    for x in range(2, R - 1):
        if maze[x, y] == ' ':
            IL = min(IL, x)
            IR = max(IR, x)
            IT = min(IT, y)
            IB = max(IB, y)

portals = defaultdict(lambda: [])
# first value in list
for y in range(2, B - 1):
    if maze[0, y] != ' ':
        portals[maze[0, y] + maze[1, y]].append((2, y))
    if maze[R, y] != ' ':
        portals[maze[R - 1, y] + maze[R, y]].append((R - 2, y))
for x in range(2, R - 1):
    if maze[x, 0] != ' ':
        portals[maze[x, 0] + maze[x, 1]].append((x, 2))
    if maze[x, B] != ' ':
        portals[maze[x, B - 1] + maze[x, B]].append((x, B - 2))

# second value in list
for y in range(IT, IB + 1):
    if maze[IL, y] != ' ':
        portals[maze[IL, y] + maze[IL + 1, y]].append((IL - 1, y))
    if maze[IR, y] != ' ':
        portals[maze[IR - 1, y] + maze[IR, y]].append((IR + 1, y))
for x in range(IL, IR + 1):
    if maze[x, IT] != ' ':
        portals[maze[x, IT] + maze[x, IT + 1]].append((x, IT - 1))
    if maze[x, IB] != ' ':
        portals[maze[x, IB - 1] + maze[x, IB]].append((x, IB + 1))

links = {}
for pp in portals.values():
    if len(pp) > 1:
        links[pp[0]] = pp[1]
        links[pp[1]] = pp[0]


def pretty():
    print()
    for y in range(B + 1):
        row = ''
        for x in range(R + 1):
            p = (x, y)
            v = maze[p]
            if p in links:
                row += '\x1b[31m+\x1b[0m'
                continue
            if p == portals['AA'][0]:
                row += '\x1b[32m+\x1b[0m'
                continue
            if p == portals['ZZ'][0]:
                row += '\x1b[34m+\x1b[0m'
                continue
            if v == ' ':
                if x == IL or x == IR:
                    row += '|'
                    continue
                if y == IT or y == IB:
                    row += '-'
                    continue
            row += v
        print(row)


pretty()

def ttoi(t): return complex(t[0], t[1])


def itot(i): return int(i.real), int(i.imag)


def ppi(p, i): return itot(ttoi(p) + i)


def walk(start, goal):
    been = defaultdict(lambda: False)
    been[start] = True
    nxt = [start]
    for step in count(1):
        if len(nxt) == 0: break
        cur, nxt = nxt, []
        sorted_list = sorted(cur)
        print(sorted_list)
        for p in cur:
            for d in [1, -1, 1j, -1j]:
                np = ppi(p, d)
                if maze[np] not in '.# ' and p in links:
                    np = links[p]
                if maze[np] == '.' and not been[np]:
                    if np == goal:
                        return step
                    been[np] = True
                    nxt.append(np)


print(walk(portals['AA'][0], portals['ZZ'][0]))
