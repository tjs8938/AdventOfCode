import re

filename = "input.txt"
# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()


class Present:

    def __init__(self, x, y, z):
        self.dims = [x, y, z]
        self.dims.sort()

    def wrapping_needed(self):
        return 3*self.dims[0]*self.dims[1] + 2*self.dims[0]*self.dims[2] + 2*self.dims[2]*self.dims[1]

    def ribbon_needed(self):
        return self.dims[0]*self.dims[1]*self.dims[2] + 2*self.dims[0] + 2*self.dims[1]


area = 0
ribbon = 0
presents = []
for line in input_lines:
    m = re.match("([0-9]*)x([0-9]*)x([0-9]*)", line)
    p = Present(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    area += p.wrapping_needed()
    ribbon += p.ribbon_needed()

print(area)
print(ribbon)
