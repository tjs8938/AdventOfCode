from typing import List, Callable

input_file = open("input.txt")
# input_file = open("test1.txt")
input_lines = input_file.read().splitlines()

total = 0


class Expression:

    def __init__(self):
        self.values: List[Expression] = []
        self.operations: List[str] = []
        self.result = None

    def __int__(self):
        if self.result is None:
            # do the thing
            self.result = 1
            while '+' in self.operations:
                index = self.operations.index('+')
                a: Expression = self.values.pop(index)
                b: Expression = self.values.pop(index)
                self.operations.pop(index)
                self.values.insert(index, a + b)

            for e in self.values:
                self.result *= int(e)

        return self.result

    def add_expression(self, e):
        self.values.append(e)

    def __add__(self, other):
        ret = Expression()
        ret.result = int(self) + int(other)
        return ret

    def __mul__(self, other):
        ret = Expression()
        ret.result = int(self) * int(other)
        return ret

    def add_operation(self, op: str):
        self.operations.append(op)


def process_math(math: str) -> int:
    current = Expression()
    stack = []
    math = math.replace(' ', '')
    for c in math:
        if c.isnumeric():
            n = Expression()
            n.result = int(c)
            current.add_expression(n)
        elif c in ['+', '*']:
            current.add_operation(c)
        elif c == '(':
            stack.append(current)
            current = Expression()
        elif c == ')':
            temp = current
            current = stack.pop()
            current.add_expression(temp)
        else:
            raise ValueError

    return int(current)


print(process_math("1 + (2 * 3) + (4 * (5 + 6))"))
print(process_math("2 * 3 + (4 * 5)"))
print(process_math("5 + (8 * 3 + 9 + 3 * 4 * 3)"))
print(process_math("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))
print(process_math("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))

for l in input_lines:
    v = process_math(l)
    total += v

print(total)
