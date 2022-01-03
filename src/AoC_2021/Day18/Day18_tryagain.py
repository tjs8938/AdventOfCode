from __future__ import annotations

import itertools
import math
from dataclasses import dataclass
from typing import Tuple

from aocd.transforms import lines

from src.aoc_frame import run_part


@dataclass(eq=False)
class Node:
    value: int
    depth: int
    left: Node = None
    right: Node = None

    def __repr__(self):
        return print_num(self)


def parse_str(snailfish_str: str, depth=0) -> Tuple[Node, Node]:
    left = None
    first = None
    for char in snailfish_str:
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
        elif char != ',':
            new_node = Node(int(char), depth)
            if first is None:
                first = new_node
                left = new_node
            else:
                left.right = new_node
                new_node.left = left
                left = new_node
    return first, left


def reduce_node(n: Node, max_depth: int):
    i = n
    # explode all pairs below the max_depth
    while i is not None:
        if i.depth > max_depth:
            pair_left = i
            pair_right = i.right
            neighbor_left = pair_left.left
            neighbor_right = pair_right.right

            if neighbor_left is not None:
                neighbor_left.value += pair_left.value
            if neighbor_right is not None:
                neighbor_right.value += pair_right.value
                neighbor_right.left = pair_left
                pair_left.right = neighbor_right
            pair_left.value = 0
            pair_left.depth -= 1
            i = neighbor_right
        else:
            i = i.right

    # split all nodes > 10, and explode if they're at max_depth
    i = n

    while i is not None:
        if i.value >= 10:
            if i.depth == max_depth:
                move_i_back = False
                # Already at max depth, split and explode in one move
                if i.left is not None:
                    i.left.value += int(math.floor(i.value / 2))
                    move_i_back = (i.left.value >= 10)
                if i.right is not None:
                    i.right.value += int(math.ceil(i.value / 2))
                i.value = 0

                if move_i_back:
                    i = i.left
            else:
                # not at max depth, so just split
                new_node = Node(int(math.ceil(i.value / 2)), i.depth + 1, left=i, right=i.right)
                if i.right is not None:
                    i.right.left = new_node
                i.right = new_node
                i.value = int(math.floor(i.value / 2))
                i.depth += 1
                i = new_node.right
        else:
            i = i.right


def mag(n: Node) -> int:
    first = n
    while first.right is not None:
        n = first
        while n is not None:
            if n.right and n.depth == n.right.depth:
                # Adjacent with the same depth, combine
                n.value = n.value * 3 + n.right.value * 2
                n.depth -= 1
                if n.right:
                    if n.right.right:
                        n.right.right.left = n
                    n.right = n.right.right
            n = n.right

    return first.value


def print_num(n: Node) -> str:
    values = str(n.value)
    depths = str(n.depth)
    i = n
    while i.right:
        i = i.right
        values += ' ' + str(i.value)
        depths += ' ' + str(i.depth)

    return values + '\n' + depths


def part_a(input_data: str) -> str:
    snail_nums = lines(input_data)
    first, end = parse_str(snail_nums[0])
    top_depth = 0
    max_depth = 3
    for next_str in snail_nums[1:]:
        print("Adding: \n" + print_num(first) + "\n")
        mid, new_end = parse_str(next_str, depth=top_depth)
        print("With: \n" + print_num(mid) + "\n")
        end.right = mid
        mid.left = end

        end = new_end
        reduce_node(first, max_depth)
        print("Resulting: \n" + print_num(first) + "\n")
        top_depth -= 1
        max_depth -= 1

    return str(mag(first))


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


run_part(part_a, 'a', 2021, 18)
# run_part(part_b, 'b', 2021, 18)
