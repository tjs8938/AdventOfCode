# Test 389125467 -> 278014356
# cups = [1, 4, 7, 5, 3, 6, 9, 8, 0]
# current = 2
# Real 685974213 -> 574863102
cups = [2, 0, 9, 1, 8, 7, 3, 4, 6]
current = 5

LARGEST = 1000000
cups.extend(list(range(10, LARGEST)))

# cups.append(2)  # Test
cups.append(5)  # Real

SIZE = len(cups)

MOVES = 10000000


def get_next_n(starting, count):
    next_n = []
    pos = starting
    for i in range(count):
        pos = cups[pos]
        next_n.append(pos)
    return next_n


def print_in_order(move):
    cups_in_order = [0]
    for i in range(1, SIZE):
        cups_in_order.append(cups[cups_in_order[-1]])

    print(str(move) + ": " + "".join(map(lambda x: str(x+1), cups_in_order)))


for i in range(MOVES):
    # print_in_order(i)
    # Get the next 4 cups (after current)
    next_4 = get_next_n(current, 4)

    # Find the destination cup (next lowest cup, wrapping around, skipping cups that are being moved
    destination = (current - 1) % SIZE
    while destination in next_4[:-1]:
        destination = (destination - 1) % SIZE

    # The current cup points to the 4th cup
    cups[current] = next_4[3]

    # The third cup points to the destinations former neighbor
    cups[next_4[2]] = cups[destination]

    # The destination points to the 1st cup
    cups[destination] = next_4[0]

    # Set current to the (former) 4th cup
    current = next_4[3]

last_indexes = get_next_n(0, 2)
print((last_indexes[0] + 1) * (last_indexes[1] + 1))