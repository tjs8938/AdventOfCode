import re

from src.Utility.MatrixPrint import pair_to_key
from src.Utility.MatrixPrint2dHex import MOVES

# input_file = open("input.txt")
input_file = open("test1.txt")
# input_file = open("test2.txt")
input_lines = input_file.read().splitlines()

pattern = re.compile("(se|sw|ne|nw|e|w)")

tiles = {}

for line in input_lines:
    position = (0, 0)
    directions = pattern.findall(line)
    for d in directions:
        position = MOVES[d](position)

    key = pair_to_key(position)
    print(key)
    if key not in tiles:
        tiles[key] = 1
    else:
        tiles[key] = tiles[key] ^ 1


total = 0
for t in tiles.values():
    total += t

print(tiles)
print(total)
