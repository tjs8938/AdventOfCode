
# inputs = [0,3,6]
# inputs = [1,3,2]
# inputs = [2,1,3]
# inputs = [1,2,3]
# inputs = [2,3,1]
# inputs = [3,2,1]
# inputs = [3,1,2]
inputs = [12,1,16,3,11,0]

last_turn = {}

for i in range(len(inputs), 2020):
    last_value = inputs[-1]
    try:
        # print(inputs[::-1][1:])
        before_that = (inputs[::-1][1:]).index(last_value) + 1
    except ValueError:
        before_that = 0
    # print(before_that)
    inputs.append(before_that)

print(inputs[-1])
