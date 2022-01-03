input_file = open("input.txt")
# input_file = open("test1.txt")
input_lines = input_file.read().splitlines()

total = 0


def math_it(value, prev_op, next_value):
    if prev_op == '+':
        return value + next_value
    else:
        return value * next_value


def process_math(line, start):
    value = 0
    prev_op = None
    index = start
    while index < len(line):
        if line[index] == '(':
            next_value, index = process_math(line, index+1)
            if prev_op is None:
                value = next_value
            else:
                value = math_it(value, prev_op, next_value)
        elif line[index] == ')':
            return value, index
        elif line[index] in ['+', '*']:
            prev_op = line[index]
        elif line[index].isnumeric():
            next_value = int(line[index])
            if prev_op is None:
                value = next_value
            else:
                value = math_it(value, prev_op, next_value)
        index += 1
    return value, index


print(process_math("2 * 3 + (4 * 5)", 0))
print(process_math("5 + (8 * 3 + 9 + 3 * 4 * 3)", 0))
print(process_math("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 0))
print(process_math("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 0))
print(process_math("9 + (1 * (2 + 3) ) * (3 + 4)", 0))


for l in input_lines:
    v, i = process_math(l, 0)
    total += v

print(total)
