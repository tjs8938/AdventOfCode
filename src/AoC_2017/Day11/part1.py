
MOVES = {'s': lambda x: (x[0], x[1] - 1),
         'nw': lambda x: (x[0] - 1, x[1]),
         'ne': lambda x: (x[0] + 1, x[1] + 1),
         'se': lambda x: (x[0] + 1, x[1]),
         'n': lambda x: (x[0], x[1] + 1),
         'sw': lambda x: (x[0] - 1, x[1] - 1)
         }


def find_steps(path: str) -> int:
    directions = path.split(',')
    position = (0, 0)

    for d in directions:
        position = MOVES[d](position)

    if position[0] < 0:
        position = (position[0] * -1, position[1] * -1)

    steps = 0
    if position[1] >= 0:
        # steps = min(position[0], position[1])
        # position = (position[0] - steps, position[1] - steps)
        steps += max(position[0], position[1])
    else:
        steps = position[0] - position[1]

    return steps


assert (find_steps('ne,ne,ne') == 3)
assert (find_steps('ne,ne,sw,sw') == 0)
assert (find_steps('ne,ne,s,s') == 2)
assert (find_steps('se,sw,se,sw,sw') == 3)

print(find_steps(open("input.txt").read()))
