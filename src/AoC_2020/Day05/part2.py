import re

filename = "input.txt"
# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()


class BoardingPass:

    def __init__(self, code):
        row_code = code[:7]
        col_code = code[7:]
        self.code = code

        self.row = 0
        self.col = 0

        for c in row_code:
            self.row *= 2
            if c == 'B':
                self.row += 1

        for c in col_code:
            self.col *= 2
            if c == 'R':
                self.col += 1

    def get_id(self):
        return self.row * 8 + self.col

    def __lt__(self, other):
        return self.get_id() < other.get_id()

    def __repr__(self):
        return "Code " + self.code + ": Row " + str(self.row) + ", Col " + str(self.col) + " = ID " + str(self.get_id())


passes = []
for line in input_lines:
    passes.append(BoardingPass(line))

passes.sort()

for i in range(0, len(passes) - 1):
    low_id = passes[i].get_id()
    if passes[i+1].get_id() == low_id + 2:
        print(low_id+1)
        break
