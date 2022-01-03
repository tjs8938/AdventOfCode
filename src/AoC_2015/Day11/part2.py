current_pw_string = "vzbxxyzz"
current_pw = []
for c in current_pw_string:
    current_pw.append(ord(c) - ord('a'))


def inc_pw():
    global current_pw
    for i in reversed(range(len(current_pw))):
        if current_pw[i] < 25:
            current_pw[i] += 1
            for j in range(i + 1, len(current_pw)):
                current_pw[j] = 0
            return


def verify_pw():
    found_straight = False
    double_index_1 = -1
    double_index_2 = -1
    for index in range(0, len(current_pw)):
        if current_pw[index] in [9, 12, 15]:
            return False
        elif index > 0:
            found_straight = found_straight or (index < len(current_pw) - 1 and
                                                current_pw[index - 1] + 1 == current_pw[index] == current_pw[index + 1] - 1)

            if current_pw[index - 1] == current_pw[index]:
                if double_index_1 < 0:
                    double_index_1 = index
                elif double_index_1 < index - 1:
                    double_index_2 = index
    return double_index_1 >= 0 and double_index_2 >= 0 and found_straight


def print_pw():
    new_pw = ""
    for i in current_pw:
        new_pw = new_pw + chr(i + ord('a'))
    print(new_pw)


while True:
    print_pw()
    inc_pw()
    if verify_pw():
        print_pw()
        break
