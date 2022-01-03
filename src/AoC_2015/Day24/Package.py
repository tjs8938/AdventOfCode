class Package:

    def __init__(self, bit_mask, present_weights):
        self.packages = []
        self.quantum_entanglement = 1
        index = 0
        while bit_mask > 0:
            if (bit_mask & 1) == 1:
                p = present_weights[index]
                self.packages.append(p)
                self.quantum_entanglement *= p
            bit_mask >>= 1
            index += 1

    def __lt__(self, other):
        len1 = len(self.packages)
        len2 = len(other.packages)
        return (len1 < len2) or (len1 == len2 and self.quantum_entanglement < other.quantum_entanglement)

