# cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]  # Test
cups = [6, 8, 5, 9, 7, 4, 2, 1, 3]  # Real

SIZE = len(cups)

MOVES = 100

for i in range(MOVES):
    current = cups[0]
    next_3 = cups[1:4]

    cups = cups[4:]
    cups.append(current)

    dest = ((current - 2) % SIZE) + 1
    while dest in next_3:
        dest = ((dest - 2) % SIZE) + 1

    index = cups.index(dest)
    prior = cups[:index+1]
    after = cups[index+1:]
    cups = prior
    cups.extend(next_3)
    cups.extend(after)
    print(cups)
