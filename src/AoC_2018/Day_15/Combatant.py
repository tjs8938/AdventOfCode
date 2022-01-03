from src.AoC_2018.Day_15.Node import Node


class Combatant:
    def __init__(self, node, name, debug):
        self.debug = debug
        self.name = name
        self.node = node
        self.hit_points = 200
        self.attack_points = 3

    @staticmethod
    def attack_order(a, b):
        if a.hit_points < b.hit_points or (a.hit_points == b.hit_points and a.node < b.node):
            return -1
        else:
            return 1

    @staticmethod
    def turn_order(a, b):
        if a.node < b.node:
            return -1
        else:
            return 1

    def __repr__(self):
        return self.name + '(' + str(self.hit_points) + ') at ' + str(self.node)

    def attack(self, enemy):
        enemy.hit_points -= min(self.attack_points, enemy.hit_points)
        if self.debug:
            print(str(self) + ' attacks ' + str(enemy))
        return enemy.hit_points <= 0

    def get_open_neighbors(self):
        result = []
        for neighbor in self.node.neighbors:
            if neighbor.combatant is None:
                result.append(neighbor)

        return result

    def move(self, path) -> Node:
        node = path.starting_point
        if self.debug:
            print(str(self) + ' moves to ' + str(node) + ' along' + str(path))
        self.node.combatant = None
        self.node = node
        node.combatant = self
        return node
