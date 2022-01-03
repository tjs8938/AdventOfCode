import re
from typing import Tuple

from src.Utility.ModularArithmetic import ModularArithmetic

DECK_SIZE = 10007

filename = "input.txt"
# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()

mod_calc = ModularArithmetic(DECK_SIZE)


def cut(f: Tuple[int, int], x: int) -> Tuple[int, int]:
    # print("Cut the deck with " + str(x) + " cards")
    return mod_calc.compose((1, -x), f)


def new_stack(f: Tuple[int, int]):
    # print("dealing new stack")
    return mod_calc.compose((-1, -1), f)


def increment(f: Tuple[int, int], x):
    return mod_calc.compose((x, 0), f)


f = (1, 0)  # initialize to the identify function

for line in input_lines:
    m = re.search("cut (.*)", line)
    if m:
        f = cut(f, int(m.group(1)))
        continue

    m = re.search("deal into new stack", line)
    if m:
        f = new_stack(f)
        continue

    m = re.search("deal with increment (.*)", line)
    if m:
        f = increment(f, int(m.group(1)))
        continue

print(mod_calc.evaluate(f, 2019))
