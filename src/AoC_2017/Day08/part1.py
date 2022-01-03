import re
from typing import Dict

# filename = "test1.txt"
filename = "input.txt"


input_line = open(filename).read().splitlines()

pattern = re.compile('(.*) (inc|dec) (.*) if (.*) (==|!=||<||>||<=||>=) (.*)')

registers: Dict[str, int] = {}

print('10') if 10 > 15 else 0


def get_value(key: str) -> int:
    return registers.get(key, 0)


def mod(register: str, command: str, value: int):
    if command == 'dec':
        value *= -1

    registers[register] = get_value(register) + value


for line in input_line:
    eval(line)

print(max(registers.values()))