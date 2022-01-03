from src.Utility.ThreadedIntCodeComputer import ThreadedIntCodeComputer


class CyclingOutputThreadedIntCodeComputer(ThreadedIntCodeComputer):
    def __init__(self, tape):
        super().__init__(tape)
        self.out_func_index = 0
        self.out_func = []

    def output(self, modes):
        o = self.get_param(True, modes[0])
        self.out_values.append(o)
        if self.out_func[self.out_func_index]:
            self.out_func[self.out_func_index](o)
        self.out_func_index = (self.out_func_index + 1) % len(self.out_func)

