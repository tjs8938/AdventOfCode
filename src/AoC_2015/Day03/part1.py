from src.Utility.MatrixPrint import pair_to_key
from src.Utility.Movement2d import move_char

filename = "input.txt"
# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()

position = (0, 0)
visited = {pair_to_key(position): 1}

for c in input_lines[0]:
    position = move_char(position, c)
    key = pair_to_key(position)
    if key not in visited:
        visited[key] = 0
    visited[key] += 1

print(len(visited))
