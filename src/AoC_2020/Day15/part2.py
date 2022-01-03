
# inputs = [0,3,6]
# inputs = [1,3,2]
# inputs = [2,1,3]
# inputs = [1,2,3]
# inputs = [2,3,1]
# inputs = [3,2,1]
# inputs = [3,1,2]
inputs = [12,1,16,3,11,0]

last_turn = {}

for i in range(len(inputs)):
    last_turn[str(inputs[i])] = [i]

last_number = inputs[-1]
print(last_number)
for i in range(len(inputs), 30000000):
    if last_turn[str(last_number)][-1] < i-1:
        last_number = i - last_turn[str(last_number)][-1] - 1
    elif len(last_turn[str(last_number)]) > 1:
        last_number = i - last_turn[str(last_number)][-2] - 1
    else:
        last_number = 0

    if str(last_number) not in last_turn:
        last_turn[str(last_number)] = []
    last_turn[str(last_number)].append(i)
    # print(last_number)

print(last_number)
