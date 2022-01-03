from enum import Enum
from inspect import signature
from typing import List, Callable, Dict


def is_number(val: str) -> bool:
    try:
        int(val)
        return True
    except ValueError:
        return False


class AssemblyComputer:

    def __init__(self, program: List[str]):
        self.registers: Dict[str, int] = {}
        self.__program_counter = 0
        self.program = program

        self.next_pc: int = None

        self.functions: Dict[str, Callable] = {}

    # Assign a function definition to an assembly code
    def register_function(self, func_name: str, function: Callable):
        self.functions[func_name] = function

    # Update the program counter with a new value
    def update_pc(self, new_pc: int):
        self.next_pc = new_pc

    # Add an offset to the program counter
    def modify_pc(self, offset: int):
        self.next_pc = self.__program_counter + offset

    # determine the value of an integer value of an input. Ints are returned, strings are looked up in the registers
    def input_value(self, arg):
        val = 0
        if is_number(arg):
            val = int(arg)
        elif arg in self.registers:
            val = self.registers[arg]
        return val

    def write_register(self, key, value):
        self.registers[key] = value

    def execute(self):
        while 0 <= self.__program_counter < len(self.program):

            self.next_pc = None
            instruction = self.program[self.__program_counter].split()
            code = instruction[0]
            sig = signature(self.functions[code])
            assert(len(sig.parameters) == len(instruction) - 1)

            self.functions[code](*instruction[1:])

            if self.next_pc is None:
                self.__program_counter += 1
            else:
                self.__program_counter = self.next_pc
