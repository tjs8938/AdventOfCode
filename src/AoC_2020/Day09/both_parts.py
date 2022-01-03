input_file = open("input.txt")
PREAMBLE = 25
# input_file = open("test1.txt")
# PREAMBLE = 5

input_lines = input_file.read().splitlines()

bad_record = -1
data = [int(x) for x in input_lines]
sums = []
for i in range(0, PREAMBLE):
    sums.append(0)
    for j in range(0, PREAMBLE):
        if i != j:
            sums.append(data[i] + data[j])

for index in range(PREAMBLE, len(data)):

    output = data[index]
    if output not in sums:
        bad_record = output
        print(output)  # part 1 answer
        break

    sums = sums[PREAMBLE:]
    for i in range(index - PREAMBLE, index):
        sums.append(data[i] + data[index])

for i in range(0, len(data)):
    running_sum = 0
    for j in range(i, len(data)):
        running_sum += data[j]
        if running_sum == bad_record:
            min_num = min(data[i:j+1])
            max_num = max(data[i:j+1])
            print(min_num + max_num)
            exit(0)
        elif running_sum > bad_record:
            break

