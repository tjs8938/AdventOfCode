import threading
from typing import List

from src.AoC_2017.Day18.DuetAssemblyComputer import DuetAssemblyComputer


class ThreadedDuetAssemblyComputer(DuetAssemblyComputer):

    def __init__(self, program: List[str], program_id: int):
        super().__init__(program)
        self.program_id = program_id
        self.mutex = threading.Lock()
        self.in_params = []
        self.sem = threading.Semaphore(0)
        self.current_in_param_index = 0
        self.out_values = []
        self.out_func = None

        self.write_register('p', program_id)

    def post_input(self, value):
        self.mutex.acquire()
        self.in_params.append(value)
        self.mutex.release()
        self.sem.release()

    def rcv(self, x):
        self.sem.acquire()
        self.mutex.acquire()
        self.write_register(x, self.in_params[self.current_in_param_index])
        self.current_in_param_index += 1
        self.mutex.release()

    def snd(self, x):
        o = self.input_value(x)
        self.out_values.append(o)
        if self.out_func:
            self.out_func(o)
        if self.program_id == 1:
            print(len(self.out_values))

