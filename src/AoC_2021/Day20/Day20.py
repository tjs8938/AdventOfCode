import itertools
from collections import defaultdict
from typing import List, Tuple, Dict

from aocd.transforms import lines

from src.Utility.MatrixPrint import tuple_dict_to_matrix, print_matrix
from src.aoc_frame import run_part


def parse_input(input_data: str) -> Tuple[List[str], Dict[Tuple[int, int], str]]:
    in_lines = lines(input_data)
    algorithm = ['0' if c == '.' else '1' for c in in_lines[0]]

    image: Dict[Tuple[int, int], str] = defaultdict(lambda: '0')
    for y in range(2, len(in_lines)):
        for x in range(len(in_lines[y])):
            image[(x, y)] = '0' if in_lines[y][x] == '.' else '1'

    return algorithm, image


def enhance_image(input_data, steps=2):
    algorithm, image = parse_input(input_data)
    for step in range(steps):
        ordered_x = sorted(map(lambda n: n[0], image.keys()))
        ordered_y = sorted(map(lambda n: n[1], image.keys()))

        new_image: Dict[Tuple[int, int], str] = defaultdict(
            lambda: '1' if step % 2 == 1 and algorithm[0] == '1' else '0')
        for y in range(ordered_y[0] - 1, ordered_y[-1] + 2):
            for x in range(ordered_x[0] - 1, ordered_x[-1] + 2):
                key = "".join([image[(x + x_off, y + y_off)]
                               for y_off, x_off in itertools.product([-1, 0, 1], repeat=2)])
                new_image[(x, y)] = algorithm[int(key, 2)]
        image = new_image
    return str(sum(map(lambda c: 1 if c == '1' else 0, image.values())))


def part_a(input_data: str) -> str:
    return enhance_image(input_data)


def part_b(input_data: str) -> str:
    return enhance_image(input_data, steps=50)


# run_part(part_a, 'a', 2021, 20)
run_part(part_b, 'b', 2021, 20)
