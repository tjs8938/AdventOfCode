import re
from typing import Dict, List

pattern = re.compile('(cpy|jnz|inc|dec) ([-0-9a-z]+)( ([-0-9a-z]+))?')


def arg_value(arg: str, registers: Dict[str, int]) -> int:
    val = 0
    if arg.isnumeric():
        val = int(arg)
    elif arg in registers:
        val = registers[arg]
    return val


def cpy(p1: str, p2: str, registers: Dict[str, int], pc: int) -> int:
    val = arg_value(p1, registers)
    registers[p2] = val

    return pc + 1


def jnz(p1: str, p2: str, registers: Dict[str, int], pc: int) -> int:
    val = arg_value(p1, registers)

    if val != 0:
        return pc + int(p2)
    else:
        return pc + 1


def inc(p1: str, registers: Dict[str, int], pc: int) -> int:
    val = arg_value(p1, registers)
    registers[p1] = val + 1

    return pc + 1


def dec(p1: str, registers: Dict[str, int], pc: int) -> int:
    val = arg_value(p1, registers)
    registers[p1] = val - 1

    return pc + 1


# filename = "test1.txt"
filename = "input.txt"

instructions: List[str] = open(filename).read().splitlines()

p_counter = 0
regs: Dict[str, int] = {}
while p_counter < len(instructions):
    m = pattern.match(instructions[p_counter])
    if m.group(1) == 'inc':
        p_counter = inc(m.group(2), regs, p_counter)
    elif m.group(1) == 'dec':
        p_counter = dec(m.group(2), regs, p_counter)
    elif m.group(1) == 'jnz':
        p_counter = jnz(m.group(2), m.group(4), regs, p_counter)
    elif m.group(1) == 'cpy':
        p_counter = cpy(m.group(2), m.group(4), regs, p_counter)

print(regs['a'])
