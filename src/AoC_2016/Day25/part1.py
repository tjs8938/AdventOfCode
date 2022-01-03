import math
import re
from typing import Dict, List

pattern = re.compile('(out|cst|cpy|jnz|inc|dec|tgl) ([-0-9a-z]+)( ([-0-9a-z]+))?')


def is_number(val: str) -> bool:
    try:
        int(val)
        return True
    except ValueError:
        return False


def arg_value(arg: str, registers: Dict[str, int]) -> int:
    val = 0
    if is_number(arg):
        val = int(arg)
    elif arg in registers:
        val = registers[arg]
    return val


def cpy(p1: str, p2: str, registers: Dict[str, int], pc: int) -> int:
    val = arg_value(p1, registers)
    if p2.isalpha():
        registers[p2] = val

    return pc + 1


def jnz(p1: str, p2: str, registers: Dict[str, int], pc: int) -> int:
    val = arg_value(p1, registers)

    if val != 0:
        return pc + arg_value(p2, registers)
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


def tgl(p1: str, registers: Dict[str, int], inst: List[str], pc: int) -> int:
    val = arg_value(p1, registers) + pc

    if val < len(inst):
        rplc = {'tgl': 'inc', 'inc': 'dec', 'dec': 'inc', 'jnz': 'cpy', 'cpy': 'jnz'}
        i = inst[val]
        inst[val] = rplc[i[:3]] + i[3:]

    return pc + 1


def cust(registers: Dict[str, int]):
    a = arg_value('a', registers)
    # cpy a d
    # cpy 7 c
    # cpy 362 b
    # inc d
    # dec b
    # jnz b -2
    # dec c
    # jnz c -5
    d = a + 2534

    registers['a'] = a
    registers['d'] = d


# filename = "test1.txt"
# regs: Dict[str, int] = {'a': 0}


filename = "input.txt"
regs: Dict[str, int] = {'a': 0}

target_signal = [0, 1, 0, 1, 0, 1]

instructions: List[str] = open(filename).read().splitlines()

a_val = 196
p_counter = 0
regs['a'] = a_val
while p_counter < len(instructions):
    m = pattern.match(instructions[p_counter])
    if m.group(1) == 'cst':
        cust(regs)
        p_counter += 1
    elif m.group(1) == 'inc':
        p_counter = inc(m.group(2), regs, p_counter)
    elif m.group(1) == 'dec':
        p_counter = dec(m.group(2), regs, p_counter)
    elif m.group(1) == 'jnz':
        p_counter = jnz(m.group(2), m.group(4), regs, p_counter)
    elif m.group(1) == 'cpy':
        p_counter = cpy(m.group(2), m.group(4), regs, p_counter)
    elif m.group(1) == 'tgl':
        p_counter = tgl(m.group(2), regs, instructions, p_counter)
    elif m.group(1) == 'out':
        print(str(a_val) + ": " + str(arg_value('a', regs)) + ", " + str(arg_value('b', regs)))
        p_counter += 1


print(a_val)