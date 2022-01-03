# filename = "test1.txt"
# SIZE = 5
filename = "input.txt"
SIZE = 256


class HashKnot:

    def __init__(self, lengths):
        self.lengths = lengths
        self.marks = [x for x in range(SIZE)]
        self.position = 0
        self.skip = 0

    @staticmethod
    def move(pos: int, dist: int) -> int:
        return (pos + dist) % SIZE

    def hash_round(self):
        for length in self.lengths:
            low = self.position
            high = HashKnot.move(self.position, length - 1)
            for i in range(int(length / 2)):
                swap = self.marks[low]
                self.marks[low] = self.marks[high]
                self.marks[high] = swap

                low = HashKnot.move(low, 1)
                high = HashKnot.move(high, -1)

            self.position = HashKnot.move(self.position, length + self.skip)
            self.skip += 1


knot = HashKnot([int(x) for x in open(filename).read().split(',')])
knot.hash_round()

print(knot.marks[0] * knot.marks[1])
