from typing import List

from src.Utility.AssemblyComputer import AssemblyComputer


class DuetAssemblyComputer(AssemblyComputer):

    # snd X plays a sound with a frequency equal to the value of X.
    def snd(self, x):

        self.played_sounds.append(self.input_value(x))

    # set X Y sets register X to the value of Y.
    def set(self, x, y):
        self.write_register(x, self.input_value(y))

    # add X Y increases register X by the value of Y.
    def add(self, x, y):
        self.write_register(x, self.input_value(x) + self.input_value(y))

    # mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
    def mul(self, x, y):
        self.write_register(x, self.input_value(x) * self.input_value(y))

    # mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y
    # (that is, it sets X to the result of X modulo Y).
    def mod(self, x, y):
        self.write_register(x, self.input_value(x) % self.input_value(y))

    # rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero,
    # the command does nothing.)
    def rcv(self, x):
        if self.input_value(x) != 0:
            print("recover " + str(self.played_sounds[-1]))

    # jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2
    # skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
    def jgz(self, x, y):
        if self.input_value(x) > 0:
            self.modify_pc(self.input_value(y))

    def __init__(self, program: List[str]):

        super().__init__(program)
        self.played_sounds = []

        self.register_function('snd', self.snd)
        self.register_function('set', self.set)
        self.register_function('add', self.add)
        self.register_function('mul', self.mul)
        self.register_function('mod', self.mod)
        self.register_function('rcv', self.rcv)
        self.register_function('jgz', self.jgz)
