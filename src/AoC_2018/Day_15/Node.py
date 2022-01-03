class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.combatant = None
        self.neighbors = []

    def __lt__(self, other):
        return self.y < other.y or (self.y == other.y and self.x < other.x)

    def __repr__(self):
        return str(self.x) + ',' + str(self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    @staticmethod
    def link_neighbors(a, b):
        a.neighbors.append(b)
        b.neighbors.append(a)

