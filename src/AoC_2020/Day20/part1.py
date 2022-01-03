import re

from src.AoC_2020.Day20.Segment import Segment
from src.Utility.MatrixPrint import print_matrix, rotate_left, flip_vertical
from src.Utility.Movement2d import NORTH, SOUTH, WEST, EAST

input_file = open("input.txt")
SIZE = 12
#
# input_file = open("test1.txt")
# SIZE = 3

input_lines = input_file.read().splitlines()

all_segments = []
index = 0
while index < len(input_lines):
    line = input_lines[index]
    seg = Segment(re.match("Tile ([0-9]*):", line).group(1))
    for i in range(10):
        index += 1
        seg.add_row(input_lines[index])

    index += 2
    all_segments.append(seg)

for i in range(len(all_segments)):
    for j in range(i + 1, len(all_segments)):
        all_segments[i].check_neighborliness(all_segments[j])

all_segments.sort()
corners = 1
for corner in all_segments[:4]:
    corners *= int(corner.tile_num)

print("Part 1: " + str(corners))

picture = [[None for j in range(SIZE)] for i in range(SIZE)]
neighbor_counts = {}
for seg in all_segments:
    c = len(seg.legal_neighbors)
    if str(c) not in neighbor_counts:
        neighbor_counts[str(c)] = []
    neighbor_counts[str(c)].append(seg)

# print(neighbor_counts)

# Populate the first row
picture[0][0] = neighbor_counts['2'][0]

# Test case - cheating to get the first square properly oriented
# picture[0][0].flip_vertical()

for i in range(1, SIZE):
    n = picture[0][i - 1]
    east = n.neighbor_orientation[EAST]
    picture[0][i] = east
    if east.neighbor_orientation[NORTH] == n:
        east.rotate_left()
    elif east.neighbor_orientation[SOUTH] == n:
        east.rotate_right()
    elif east.neighbor_orientation[EAST] == n:
        east.flip_horizontal()

    if n.get_right() == east.get_left():
        east.flip_vertical()

for j in range(1, SIZE):
    for i in range(SIZE):
        n = picture[j - 1][i]
        south = n.neighbor_orientation[SOUTH]
        picture[j][i] = south
        if south.neighbor_orientation[EAST] == n:
            south.rotate_left()
        elif south.neighbor_orientation[WEST] == n:
            south.rotate_right()
        elif south.neighbor_orientation[SOUTH] == n:
            south.flip_vertical()

        if n.get_bottom() == south.get_top():
            south.flip_horizontal()


def fill_out(pic_blocks):
    result = []
    for y in range(len(pic_blocks)):
        for x in range(len(pic_blocks[y])):
            for inner_y in range(0, len(pic_blocks[y][x].rows) - 2):
                if x == 0:
                    result.append("")
                for inner_x in range(0, len(pic_blocks[y][x].rows[inner_y]) - 2):
                    result[y * 8 + inner_y] += (pic_blocks[y][x].rows[inner_y + 1][inner_x + 1])
    return result


full_picture = fill_out(picture)

monster_top = re.compile("(.{18})#(.)")
monster_mid = re.compile("#(.{4})##(.{4})##(.{4})###")
monster_btm = re.compile("(.)#(..)#(..)#(..)#(..)#(..)#(...)")

monster_count = 0


def count_monsters(pic):
    count = 0
    for y in range(len(pic) - 2):
        for x in range(len(pic[y]) - 20):
            top_match = monster_top.match(pic[y][x:x + 20])
            mid_match = monster_mid.match(pic[y + 1][x:x + 20])
            btm_match = monster_btm.match(pic[y + 2][x:x + 20])
            if top_match and mid_match and btm_match:
                count += 1
                pic[y] = pic[y][:x] + 'O'.join(top_match.groups()) + pic[y][x + 20:]
                pic[y + 1] = pic[y + 1][:x] + 'O' + mid_match.group(1) + 'OO' + mid_match.group(2) + 'OO' \
                             + mid_match.group(3) + 'OOO' + pic[y + 1][x + 20:]
                pic[y + 2] = pic[y + 2][:x] + 'O'.join(btm_match.groups()) + pic[y + 2][x + 20:]
    return count


for i in range(8):
    monster_count = count_monsters(full_picture)
    if monster_count > 0:
        break

    if i == 4:
        full_picture = flip_vertical(full_picture)
    full_picture = rotate_left(full_picture)

print_matrix(full_picture)

pound_count = 0
for row in full_picture:
    pound_count += row.count('#')
print(pound_count)
