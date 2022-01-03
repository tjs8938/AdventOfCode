puzzle_input = 348

buffer = [0]
current_pos = 0


def print_in_order():
    string = "0 "
    pos = 0
    while buffer[pos] != 0:
        string += str(buffer[pos]) + ' '
        pos = buffer[pos]
    print(string)


for i in range(1, 50_000_000):

    # spin
    for steps in range(puzzle_input % len(buffer)):
        current_pos = buffer[current_pos]

    buffer.append(buffer[current_pos])
    buffer[current_pos] = i
    current_pos = len(buffer) - 1

    # print(buffer)
print(buffer[0])