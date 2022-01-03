from src.Utility.ThreadedIntCodeComputer import ThreadedIntCodeComputer


class AsciiIntCodeComputer(ThreadedIntCodeComputer):

    def __init__(self, tape):
        super().__init__(tape)
        self.output_strings = [""]
        self.out_func = self.handle_output

    def handle_output(self, out_code):
        if out_code == 10:
            print(self.output_strings[-1])
            self.output_strings.append("")
        else:
            self.output_strings[-1] = self.output_strings[-1] + chr(out_code)

    def accept_str_input(self, input_str: str):
        for c in input_str:
            self.post_input(ord(c))
        self.post_input(10)
