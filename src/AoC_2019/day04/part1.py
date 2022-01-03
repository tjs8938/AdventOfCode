num_length = 6

start = 236665
end = 713787


def next_num(i):
    str_rep = list(str(i+1))
    for digit in range(0, num_length-1):
        while str_rep[digit] > str_rep[digit + 1]:
            str_rep[digit + 1] = str(int(str_rep[digit + 1]) + 1)

    new_value = int("".join(str_rep))
    if len(set(str_rep)) < num_length:
        print(new_value)
        return new_value
    else:
        return next_num(new_value)


good_values = []
current = next_num(start)
while current < end:
    good_values.append(current)
    current = next_num(current)

print(len(good_values))
