from aocd.transforms import lines

from src.Utility.MatrixPrint import print_matrix, tuple_dict_to_matrix
from src.aoc_frame import run_part


def part_a(input_data: str) -> str:

    points = {}
    instructions = []
    for l in lines(input_data):
        if ',' in l:
            x, y = l.split(',')
            points[(int(x), int(y))] = '#'
        elif '=' in l:
            instructions.append(l)

    instruction = instructions[0].split()[-1].split('=')
    axis = 0 if instruction[0] == 'x' else 1
    position = int(instruction[1])

    new_points = []
    for location in points:
        if location[axis] > position:
            points[location] = '.'
            x = location[0]
            y = location[1]
            if axis == 0:
                x = 2 * position - x
            else:
                y = 2 * position - y
            new_points.append((x, y))

    for new_p in new_points:
        points[new_p] = '#'

    count = 0
    for dot in points.values():
        if dot == '#':
            count += 1
    return str(count)


def part_b(input_data: str) -> str:
    points = {}
    instructions = []
    for l in lines(input_data):
        if ',' in l:
            x, y = l.split(',')
            points[(int(x), int(y))] = '#'
        elif '=' in l:
            instructions.append(l)

    for i in range(len(instructions)):
        instruction = instructions[i].split()[-1].split('=')
        axis = 0 if instruction[0] == 'x' else 1
        position = int(instruction[1])

        new_points = []
        del_points = []
        for location in points:
            if location[axis] > position and points[location] == '#':
                del_points.append(location)
                x = location[0]
                y = location[1]
                if axis == 0:
                    x = 2 * position - x
                else:
                    y = 2 * position - y
                new_points.append((x, y))

        for new_p in new_points:
            points[new_p] = '#'
        for old_p in del_points:
            del points[old_p]

    # Personal email
    code = "AHPRPAUZ"

    # Solu email
    # code = "RZKZLPGH"
    filled_matrix = tuple_dict_to_matrix(points)
    print_matrix(filled_matrix)
    return code


# run_part(part_a, 'a', 2021, 13)
run_part(part_b, 'b', 2021, 13)

