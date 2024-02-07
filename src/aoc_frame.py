import json
import os
import sys
import time
from typing import Callable

from aocd import submit
from aocd.models import Puzzle, User

user_tokens = {
    'Personal gmail': '53616c7465645f5f5dfb60fe167571b808233e37a155356b8d7a5bff35c7cad035ac48b72ee67fb75b6d47891c65d7db5ccbd9de408e13011b659d7950e150d1',
    'Solu gmail': '53616c7465645f5ffc7a5b1e3314922dfa8d99a67ee81ece736a52c29674200e3769e3d145dc5b4b474fae38864e3e76964b878ddf431ce3f9d9dc3bec58c544'}


def frame_print(output: str):
    print(output, file=sys.__stdout__)


def run_part(operation: Callable[[str], str], part: str, year: int, day: int, test=True, debug=True):
    frame_print("Starting execution for {} Day {}, part {}".format(year, day, part))
    if not debug:
        sys.stdout = open(os.devnull, 'w')
    unit_test_dir = '../../AoC_' + str(year) + '/Day' + "{:02d}".format(day) + '/unittest'
    if test and os.path.isdir(unit_test_dir):

        for file in os.listdir(unit_test_dir):
            with open(os.path.join(unit_test_dir, file), 'r') as testfile:
                json_object = json.load(testfile)

            if part in json_object:
                frame_print("*** Running unit test from file " + file)
                start_time = time.time()

                result = str(operation(json_object['input_data']))
                print("Executed in " + str(time.time() - start_time))

                if json_object[part] != result:
                    print("Expected: " + json_object[part] + ", Got: " + result)
                    exit(1)

    for name, token in user_tokens.items():
        frame_print('*** Solving for account: ' + name)
        start_time = time.time()
        user = User(token)
        puzzle = Puzzle(year=year, day=day, user=user)
        answer = operation(puzzle.input_data)
        sys.stdout = sys.__stdout__
        print("Part " + part + " executed in " + str(time.time() - start_time))
        submit(answer, part=part, year=year, day=day, session=token)

    frame_print('-------------------------------------------------------------')


def gen_challenge_files(year: int):
    for day in range(1, 26):
        day_str = "Day{:02d}".format(day)
        os.makedirs(os.path.join('AoC_' + str(year), day_str, "unittest"), exist_ok=True)

        file_path = os.path.join('AoC_' + str(year), day_str, day_str + '.py')
        if not os.path.isfile(file_path) or os.stat(file_path).st_size == 0:
            with open(os.path.join('AoC_' + str(year), day_str, day_str + '.py'), 'w') as output_file, \
                    open('puzzle_template') as template_file:
                template = template_file.read()
                print(template.format(year=year, day=day), file=output_file)


def gen_challenge_files_kotlin(year: int):
    for day in range(9, 26):
        day_str = "Day{:02d}".format(day)

        file_path = os.path.join('AoC_' + str(year), day_str + '.kt')
        if not os.path.isfile(file_path) or os.stat(file_path).st_size == 0:
            with open(file_path, 'w') as output_file,  open('kotlin_template') as template_file:
                template = template_file.read()
                print(template.format(year=year, day=day, class_name=day_str), file=output_file)


gen_challenge_files_kotlin(2022)
