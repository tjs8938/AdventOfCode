from __future__ import annotations

import itertools
import math
from dataclasses import dataclass

from aocd.transforms import lines

from src.aoc_frame import run_part


@dataclass(eq=False)
class Node:
    value: int = -1
    left: Node = None
    right: Node = None
    parent: Node = None

    def __repr__(self):
        if self.value >= 0:
            return str(self.value)
        else:
            return '[' + str(self.left) + ',' + str(self.right) + ']'

    def mag(self) -> int:
        if self.value >= 0:
            return self.value
        else:
            return self.left.mag() * 3 + self.right.mag() * 2


def parse_str(snailfish_str: str) -> Node:
    assert snailfish_str[0] == '[' and snailfish_str[-1] == ']'
    n = Node()
    for char in snailfish_str[1:-1]:
        if char == '[':
            new_node = Node()
            new_node.parent = n
            if n.left is None:
                n.left = new_node
            else:
                n.right = new_node
            n = new_node
        elif char == ']':
            n = n.parent
        elif char != ',':
            new_node = Node(value=int(char), parent=n)
            if n.left is None:
                n.left = new_node
            else:
                n.right = new_node
    return n


def explode(n):
    last_node = None
    current_node = n
    depth = 0
    last_value_node = None
    carry_right = -1
    exploded = False
    while True:
        if current_node.value == -1 and depth == 4 and not exploded:
            # Explode!
            if last_value_node is not None:
                last_value_node.value += current_node.left.value
            carry_right = current_node.right.value
            exploded = True
            current_node.value = 0
            current_node.left = None
            current_node.right = None
            last_node = current_node
            current_node = current_node.parent
            depth -= 1

        elif current_node.value >= 0:
            if carry_right >= 0:
                current_node.value += carry_right
                break
            last_value_node = current_node
            last_node = current_node
            current_node = current_node.parent
            depth -= 1
            continue

        elif last_node == current_node.right:
            if current_node.parent is None:
                return exploded
            else:
                last_node = current_node
                current_node = current_node.parent
            depth -= 1
        elif last_node is None or last_node == current_node.parent:
            last_node = current_node
            current_node = current_node.left
            depth += 1
        elif last_node == current_node.left:
            last_node = current_node
            current_node = current_node.right
            depth += 1

    return exploded


def split_node(n) -> bool:
    last_node = None
    current_node = n
    while True:
        if current_node.value >= 0:
            if current_node.value >= 10:
                current_node.left = Node(value=math.floor(current_node.value / 2), parent=current_node)
                current_node.right = Node(value=math.ceil(current_node.value / 2), parent=current_node)
                current_node.value = -1
                return True
            else:
                last_node = current_node
                current_node = current_node.parent
                continue

        if last_node == current_node.right:
            if current_node.parent is None:
                return False
            else:
                last_node = current_node
                current_node = current_node.parent
        elif last_node is None or last_node == current_node.parent:
            last_node = current_node
            current_node = current_node.left
        elif last_node == current_node.left:
            last_node = current_node
            current_node = current_node.right


def reduce_node(n: Node):
    split = True
    while split:
        exploded = True
        while exploded:
            exploded = explode(n)
        split = split_node(n)
    pass


def part_a(input_data: str) -> str:
    snail_nums = lines(input_data)
    n = parse_str(snail_nums[0])
    for next_str in snail_nums[1:]:
        next_node = parse_str(next_str)
        parent = Node(left=n, right=next_node)
        n.parent = parent
        next_node.parent = parent
        reduce_node(parent)
        n = parent

    return str(n.mag())


def part_b(input_data: str) -> str:
    snail_nums = lines(input_data)
    best_mag = 0
    for a, b in itertools.permutations(snail_nums, 2):
        node_a = parse_str(a)
        node_b = parse_str(b)
        parent = Node(left=node_a, right=node_b)
        node_a.parent = parent
        node_b.parent = parent
        reduce_node(parent)
        mag = parent.mag()
        if mag > best_mag:
            best_mag = mag

    return str(best_mag)


# run_part(part_a, 'a', 2021, 18)
run_part(part_b, 'b', 2021, 18)
