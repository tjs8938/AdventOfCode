import re


class GameCodeComputer:

    inst_regex = re.compile("([a-z]*) ([+\-][0-9]*)")

    def __init__(self, code):
        self.code = code
        self.inst_ptr = 0
        self.accumulator = 0
        self.debug_func = None

    def nop(self, value):
        self.inst_ptr += 1

    def acc(self, value):
        self.accumulator += value
        self.inst_ptr += 1

    def jmp(self, value):
        self.inst_ptr += value

    def run(self):
        while self.inst_ptr < len(self.code):
            m = GameCodeComputer.inst_regex.match(self.code[self.inst_ptr])
            instruction = m.group(1)
            value = int(m.group(2))
            eval("self." + instruction)(value)
            if self.debug_func is not None:
                if self.debug_func(value) == -1:
                    return -1

        return self.accumulator
