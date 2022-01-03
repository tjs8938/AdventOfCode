from dataclasses import dataclass
from typing import Tuple


@dataclass
class ModularArithmetic:
    modulus: int

    def add(self, x: int, y: int):
        return (x + y) % self.modulus

    def multiply(self, x: int, y: int):
        if x == 0:
            return 0
        elif x == 1:
            return y
        else:
            half = self.multiply(x // 2, y)
            two_half = self.add(half, half)
            if x % 2 == 1:
                return self.add(two_half, y)
            else:
                return two_half

    # calculate x^y mod m
    def pow(self, x: int, y: int):
        if y == 0:
            return 1
        elif y == 1:
            return x
        else:
            half = self.pow(x, y // 2)
            two_half = self.multiply(half, half)
            if y % 2 == 1:
                return self.multiply(two_half, x)
            else:
                return two_half

    # calculate a/b mod m
    def divide(self, a, b):
        # a/b mod m == a * b^(m-2) mod m
        inv_b = self.pow(b, self.modulus - 2)
        return self.multiply(a, inv_b)

    # Compose [f(x) = ax + b mod m] and [g(x) = cx + d mod m] into g(f((x)) = c(ax + b) + d mod m = acx + bc + d mod m
    def compose(self, g: Tuple[int, int], f: Tuple[int, int]) -> Tuple[int, int]:
        a, b = f
        c, d = g
        new_a = self.multiply(a, c)
        new_b = self.multiply(b, c)
        new_b = self.add(new_b, d)
        return new_a, new_b

    # Calculate f^a(x)
    def pow_compose(self, f: Tuple[int, int], a: int) -> Tuple[int, int]:
        if a == 0:
            return 1, 0
        if a == 1:
            return f
        else:
            half = self.pow_compose(f, a // 2)
            two_half = self.compose(half, half)
            if a % 2 == 1:
                return self.compose(two_half, f)
            else:
                return two_half

    # Invert f(x)
    def invert_function(self, f: Tuple[int, int], x) -> int:
        # F(x) = Ax + B
        # F^-1(x) = (x - B) / A
        return self.divide(self.add(x, -f[1]), f[0])

    def evaluate(self, f: Tuple[int, int], x: int):
        # return f(x) mod m
        return self.add(self.multiply(f[0], x), f[1])


mod_calc = ModularArithmetic(7)
assert(mod_calc.add(6, 5) == 4)
assert(mod_calc.multiply(6, 5) == 2)
assert(mod_calc.pow(2, 5) == 4)
assert(mod_calc.divide(5, 3) == 4)