
# filename = "test1.txt"
filename = "input.txt"


input_lines = open(filename).read().splitlines()
sum = 0

for line in input_lines:
    nums = sorted(map(lambda x: int(x), line.split()))

    for d in range(len(nums) - 1):
        for n in range(d + 1, len(nums)):
            if nums[n] % nums[d] == 0:
                sum += int(nums[n] / nums[d])

print(sum)
