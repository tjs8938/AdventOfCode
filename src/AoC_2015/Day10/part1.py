

number = "1113222113"

for i in range(0, 50):
    new_number = ""
    last_char = number[0]
    count = 1
    for c in number[1:]:
        if c == last_char:
            count += 1
        else:
            new_number = new_number + str(count) + last_char
            last_char = c
            count = 1

    number = new_number + str(count) + last_char
    print(len(number))

print(len(number))
