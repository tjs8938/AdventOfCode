# filename = "input.txt"
# TARGET = 150
filename = "test1.txt"
TARGET = 25

file = open(filename)
input_lines = file.read().splitlines()


pails = {}
for i in range(len(input_lines)):
    pails[str(pow(2, i))] = int(input_lines[i])
    pails[str(0 - pow(2, i))] = int(input_lines[i])
# print(pails)


def gray(n: int) -> int:
    return n ^ (n >> 1)


counter = 0
rolling_sum = 0
for i in range(1, pow(2, len(input_lines))):
    # print("{:05b} - {:05b} = {}".format(gray(i), gray(i - 1), gray(i) - gray(i - 1)))
    toggle = gray(i) - gray(i - 1)
    amount = pails[str(toggle)]
    if toggle > 0:
        rolling_sum += amount
    else:
        rolling_sum -= amount
    if rolling_sum == TARGET:
        counter += 1

print(counter)
