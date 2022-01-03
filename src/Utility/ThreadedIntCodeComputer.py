import math
import threading


class ThreadedIntCodeComputer(threading.Thread):
    param_counts = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]

    def __init__(self, tape):
        super().__init__()
        self.mutex = threading.Lock()
        self.in_params = []
        self.sem = threading.Semaphore(0)
        self.current_in_param_index = 0
        self.out_values = []
        self.out_func = None
        self.halt_func = None
        self.tape = tape
        self.pc = 0
        self.relative_base = 0
        self.debug = False

    def post_input(self, value):
        self.mutex.acquire()
        self.in_params.append(value)
        self.mutex.release()
        self.sem.release()

    def add(self, modes):
        addend1 = self.get_param(True, modes[0])
        addend2 = self.get_param(True, modes[1])
        self.tape[self.get_param(False, modes[2])] = addend1 + addend2

    def multiply(self, modes):
        factor1 = self.get_param(True, modes[0])
        factor2 = self.get_param(True, modes[1])
        self.tape[self.get_param(False, modes[2])] = factor1 * factor2

    def input(self, modes):
        self.sem.acquire()
        self.mutex.acquire()
        self.tape[self.get_param(False, modes[0])] = self.in_params[self.current_in_param_index]
        self.current_in_param_index += 1
        self.mutex.release()

    def output(self, modes):
        o = self.get_param(True, modes[0])
        self.out_values.append(o)
        if self.out_func:
            self.out_func(o)

    def jump_if_true(self, modes):
        value = self.get_param(True, modes[0])
        position = self.get_param(True, modes[1])
        if value != 0:
            self.pc = position

    def jump_if_false(self, modes):
        value = self.get_param(True, modes[0])
        position = self.get_param(True, modes[1])
        if value == 0:
            self.pc = position

    def less_than(self, modes):
        value1 = self.get_param(True, modes[0])
        value2 = self.get_param(True, modes[1])
        self.tape[self.get_param(False, modes[2])] = 1 if value1 < value2 else 0

    def equals(self, modes):
        value1 = self.get_param(True, modes[0])
        value2 = self.get_param(True, modes[1])
        self.tape[self.get_param(False, modes[2])] = 1 if value1 == value2 else 0

    def adjust_rel_base(self, modes):
        self.relative_base += self.get_param(True, modes[0])

    def parse_instruction(self):
        instruction = self.tape[self.pc]
        opcode = instruction % 100  # grab the last 2 digits of the pc as the opcode
        param_count = ThreadedIntCodeComputer.param_counts[opcode]

        if self.debug:
            print("Computer {} - {}".format(self.in_params[0], self.tape[self.pc:self.pc+param_count+1]))

        self.pc += 1

        modes = []
        if opcode != 99:
            # The hundreds digit is the parameter mode for the first parameter, and each digit above that is used as the
            # parameter mode for successive parameters
            divisor = 100
            for p_count in range(0, param_count):
                modes.append(math.floor(instruction / divisor) % 10)
                divisor *= 10

        return opcode, modes

    def get_param(self, input_param, mode):
        address = 0
        if mode == 0:
            address = self.tape[self.pc]
        elif mode == 1:
            address = self.pc
        elif mode == 2:
            address = self.tape[self.pc] + self.relative_base

        if address >= len(self.tape):
            self.tape.extend([0] * (address - len(self.tape) + 1))

        self.pc += 1
        return self.tape[address] if input_param else address

    def run(self):
        while self.tape[self.pc] != 99:
            opcode, parameters = self.parse_instruction()
            if opcode == 1:
                self.add(parameters)
            elif opcode == 2:
                self.multiply(parameters)
            elif opcode == 3:
                self.input(parameters)
            elif opcode == 4:
                self.output(parameters)
            elif opcode == 5:
                self.jump_if_true(parameters)
            elif opcode == 6:
                self.jump_if_false(parameters)
            elif opcode == 7:
                self.less_than(parameters)
            elif opcode == 8:
                self.equals(parameters)
            elif opcode == 9:
                self.adjust_rel_base(parameters)
            else:
                break

        if self.halt_func:
            self.halt_func()
