from src.Utility.MatrixPrint import pair_to_key
from src.Utility.Movement2d import move_char

filename = "input.txt"
# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()

index = 0
position = [(0, 0), (0, 0)]
visited = {pair_to_key(position[0]): 2}

for c in input_lines[0]:
    position[index] = move_char(position[index], c)
    key = pair_to_key(position[index])
    if key not in visited:
        visited[key] = 0
    visited[key] += 1
    index = index ^ 1

print(visited)
print(len(visited))
