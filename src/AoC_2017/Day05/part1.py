from typing import List

# filename = "test1.txt"
filename = "input.txt"


input_lines = open(filename).read().splitlines()

instructions: List[int] = [int(x) for x in input_lines]
pc = 0
steps = 0

while 0 <= pc < len(instructions):
    jump = instructions[pc]
    instructions[pc] += 1
    pc += jump
    steps += 1

print(steps)