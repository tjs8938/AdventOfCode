from math import floor

INPUT = 3014387


class Elf:

    def __init__(self, id: int):
        self.id = id
        self.neighbor = None
        self.other_neighbor = None


thief = Elf(1)
victim = None
last_node = thief
for i in range(1, INPUT):
    node = Elf(i + 1)
    last_node.neighbor = node
    node.other_neighbor = last_node

    if floor(INPUT / 2) == i:
        victim = node

    last_node = node

last_node.neighbor = thief
thief.other_neighbor = last_node

parity = INPUT % 2
while thief.neighbor.neighbor != thief:
    # "Increment" the victim
    new_victim = victim.neighbor
    if parity > 0:
        new_victim = new_victim.neighbor
    parity ^= 1

    # Remove the victim from the ring
    victim.neighbor.other_neighbor = victim.other_neighbor
    victim.other_neighbor.neighbor = victim.neighbor

    victim = new_victim

    # move to the next thief
    thief = thief.neighbor

print(thief.id)
