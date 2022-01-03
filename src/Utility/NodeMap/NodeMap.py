from typing import List, Dict, Callable, TypeVar, Generic

from src.Utility.MatrixPrint import position_to_key
from src.Utility.Movement2d import WEST, EAST, SOUTH, NORTH
from src.Utility.NodeMap.Node import Node

T = TypeVar('T')


class NodeMap(Generic[T]):

    def __init__(self, text_map: List[str], node_gen: Callable[[int, int, str], T], blocked=None, empty=None):
        if blocked is None:
            blocked = ['#']
        if empty is None:
            empty = ['.', ' ']
        self.nodes: Dict[str, Node] = {}
        self.locations: Dict[str, Node] = {}

        for y in range(len(text_map)):
            for x in range(len(text_map[y])):
                symbol = text_map[y][x]
                if symbol not in blocked:
                    n = node_gen(x, y, symbol)
                    self.nodes[position_to_key(x, y)] = n

                    if symbol not in empty:
                        self.locations[symbol] = n

                    west_neighbor_key = position_to_key(x - 1, y)
                    north_neighbor_key = position_to_key(x, y - 1)

                    if west_neighbor_key in self.nodes:
                        n.set_neighbor(self.nodes[west_neighbor_key], WEST)
                        self.nodes[west_neighbor_key].set_neighbor(n, EAST)
                    if north_neighbor_key in self.nodes:
                        n.set_neighbor(self.nodes[north_neighbor_key], NORTH)
                        self.nodes[north_neighbor_key].set_neighbor(n, SOUTH)

    def get_node(self, x: int, y: int) -> Node:
        return self.nodes.get(position_to_key(x, y))

    def get_node_by_key(self, key: str) -> Node:
        return self.locations[key]
