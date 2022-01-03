# filename = "test1.txt"
from typing import List, Set, Dict

# filename = "test1.txt"
filename = "input.txt"


input_line = open(filename).read().splitlines()[0]

blocks: List[int] = [int(x) for x in input_line.split()]

past_states: Dict[str, int] = {','.join(input_line.split()): 0}

cycles = 0

while True:
    cycles += 1

    # Find block with most memory
    index = 0
    most_mem = 0
    for b in range(len(blocks)):
        if blocks[b] > most_mem:
            most_mem = blocks[b]
            index = b

    # redistribute the memory
    blocks[index] = 0
    while most_mem > 0:
        index = (index + 1) % len(blocks)
        blocks[index] += 1
        most_mem -= 1

    # convert state to string
    current_state = ",".join(map(lambda x: str(x), blocks))
    if current_state in past_states:
        print(cycles - past_states[current_state])
        break
    else:
        past_states[current_state] = cycles
