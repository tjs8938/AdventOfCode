import re


class Reaction(object):
    def __init__(self, in_str):
        m = re.match(r'(.*) => (\d+) ([A-Z]+)', in_str)
        inputs = m.group(1)
        self.output_count = int(m.group(2))
        self.output_type = m.group(3)

        self.inputs = {}
        for i in re.findall(r'(\d+) ([A-Z]+)', inputs):
            self.inputs[i[1]] = int(i[0])

    def __repr__(self) -> str:
        return "Inputs: " + str(self.inputs) + ", Outputs: " + str(self.output_count) + " " + self.output_type
