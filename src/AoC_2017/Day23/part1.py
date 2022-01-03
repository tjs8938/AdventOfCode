from typing import List

from src.Utility.AssemblyComputer import AssemblyComputer


class Tablet(AssemblyComputer):

    def set(self, x, y):
        self.write_register(x, self.input_value(y))

    def sub(self, x, y):
        self.write_register(x, self.input_value(x) - self.input_value(y))

    def mul(self, x, y):
        self.write_register(x, self.input_value(x) * self.input_value(y))
        self.mul_count += 1

    def jnz(self, x, y):
        if self.input_value(x) != 0:
            self.modify_pc(self.input_value(y))

    def __init__(self, program: List[str]):
        super().__init__(program)
        self.register_function('set', self.set)
        self.register_function('sub', self.sub)
        self.register_function('mul', self.mul)
        self.register_function('jnz', self.jnz)
        self.mul_count = 0


tablet = Tablet(open("input.txt").read().splitlines())
tablet.execute()

print(tablet.mul_count)
