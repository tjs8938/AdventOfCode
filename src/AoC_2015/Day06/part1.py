import re

NORTH = 0
WEST = 1
SOUTH = 2
EAST = 3

L_SAME = 0
H_SAME = 1
L_OPPO = 2
H_OPPO = 3
# lower same-axis, upper same-axis, lower opposite-axis, upper opposite-axis
related_dirs = [(NORTH, SOUTH, WEST, EAST),
                (WEST, EAST, NORTH, SOUTH),
                (NORTH, SOUTH, WEST, EAST),
                (WEST, EAST, NORTH, SOUTH)]


class LightBlock:

    def __init__(self, nw_corner, se_corner):
        self.se_corner = se_corner
        self.nw_corner = nw_corner

    def get_edge(self, direction):
        if direction == NORTH:
            return self.nw_corner[1]
        if direction == WEST:
            return self.nw_corner[0]
        if direction == SOUTH:
            return self.se_corner[1]
        if direction == EAST:
            return self.se_corner[0]

    def get_light_count(self):
        return (self.get_edge(EAST) - self.get_edge(WEST) + 1) * (self.get_edge(SOUTH) - self.get_edge(NORTH) + 1)


filename = "input.txt"
# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()

flip_state = {'on': 'off', 'off': 'on'}
lights = {'on': [], 'off': [LightBlock((0, 0), (999, 999))]}


def find_overlaps(section, changing_section):
    overlaps = []
    for direction in range(0, 4):
        if section.get_edge(related_dirs[direction][L_OPPO]) <= changing_section.get_edge(related_dirs[direction][H_OPPO]) \
                and section.get_edge(related_dirs[direction][H_OPPO]) >= changing_section.get_edge(related_dirs[direction][L_OPPO]) \
                and section.get_edge(related_dirs[direction][L_SAME]) < changing_section.get_edge(direction) < section.get_edge(related_dirs[direction][H_SAME]):
            overlaps.append(direction)

    return overlaps


def split_section(section, changing_section, state):
    overlap_directions = find_overlaps(section, changing_section)
    # no overlaps, so return the original section with the original state
    if len(overlap_directions) == 0:
        return {state: [section]}

    # Overlaps were found, so address each one
    new_sections = {'on': [], 'off': []}
    for direction in overlap_directions:
        new_nw = section.nw_corner
        new_se = section.se_corner

        if direction == WEST:
            new_se = (changing_section.get_edge(WEST) - 1, section.get_edge(SOUTH))
        elif direction == EAST:
            new_nw = (changing_section.get_edge(EAST) + 1, section.get_edge(NORTH))
        elif direction == NORTH:
            new_nw = (max(section.get_edge(WEST), changing_section.get_edge(WEST)), section.get_edge(NORTH))
            new_se = (min(section.get_edge(EAST), changing_section.get_edge(EAST)), changing_section.get_edge(NORTH) - 1)
        elif direction == SOUTH:
            new_nw = (max(section.get_edge(WEST), changing_section.get_edge(WEST)), changing_section.get_edge(SOUTH) + 1)
            new_se = (min(section.get_edge(EAST), changing_section.get_edge(EAST)), section.get_edge(SOUTH))

        new_sections[state].append(LightBlock(new_nw, new_se))

    # now handle the overlapping section that goes in the opposite state
    new_nw = (max(section.get_edge(WEST), changing_section.get_edge(WEST)), max(section.get_edge(NORTH), changing_section.get_edge(NORTH)))
    new_se = (min(section.get_edge(EAST), changing_section.get_edge(EAST)), min(section.get_edge(SOUTH), changing_section.get_edge(SOUTH)))
    new_sections[flip_state[state]].append(LightBlock(new_nw, new_se))

    return new_sections


for line in input_lines:
    new_lights = []
    counter = 0

    m = re.match(".*(on|off|toggle) ([0-9]*),([0-9]*) through ([0-9]*),([0-9]*)", line)
    op = m.group(1)
    x1 = int(m.group(2))
    y1 = int(m.group(3))
    x2 = int(m.group(4))
    y2 = int(m.group(5))
    changing_section = LightBlock((x1, y1), (x2, y2))

    for state in lights:
        if state != op:
            temp_list = lights[state]
            lights[state] = []
            for section in temp_list:
                light_map = split_section(section, changing_section, state)
                for new_state in light_map:
                    lights[new_state].extend(light_map[new_state])

total = 0
for section in lights['on']:
    total += section.get_light_count()

print(total)
