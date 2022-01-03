
# filename = "test1.txt"
filename = "input.txt"


input_lines = open(filename).read().splitlines()
sum = 0

for line in input_lines:
    nums = sorted(map(lambda x: int(x), line.split()))
    sum += nums[-1] - nums[0]

print(sum)