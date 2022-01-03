
class Elf:

    def __init__(self, id: int):
        self.id = id
        self.neighbor = None


first_node = Elf(1)
last_node = first_node
for i in range(1, 3014387):
    node = Elf(i+1)
    last_node.neighbor = node
    last_node = node

last_node.neighbor = first_node

node = first_node
while node.neighbor.neighbor != node:
    node.neighbor = node.neighbor.neighbor
    node = node.neighbor

print(node.id)
