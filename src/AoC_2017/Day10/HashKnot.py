import functools


SIZE = 256


class HashKnot:

    def __init__(self, string):
        self.lengths = []
        for c in string:
            self.lengths.append(ord(c))

        self.lengths.extend([17, 31, 73, 47, 23])

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

    def hash(self) -> str:
        hash_string = ''
        for i in range(64):
            self.hash_round()

        for block in range(16):
            dense = functools.reduce(lambda a, b: a ^ b, self.marks[block * 16: (block + 1) * 16])
            hash_string += hex(dense)[2:].zfill(2)

        return hash_string
