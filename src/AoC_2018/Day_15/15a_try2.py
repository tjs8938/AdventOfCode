#!/bin/python
import heapq
import time
from collections import deque
from datetime import datetime
from functools import cmp_to_key
from typing import List

from src.AoC_2018.Day_15.Combatant import Combatant
from src.AoC_2018.Day_15.Node import Node
from src.AoC_2018.Day_15.Path import Path


def combat(filename: str, debug, elf_attack_points=3):
    file = open(filename, 'r')

    def print_map():
        for print_line in node_map:
            row = ""
            fighters = []
            for print_node in print_line:
                if print_node is None:
                    row += '#'
                elif print_node.combatant is None:
                    row += '.'
                elif print_node.combatant in goblins:
                    row += 'G'
                    fighters.append(print_node.combatant)
                elif print_node.combatant in elves:
                    row += 'E'
                    fighters.append(print_node.combatant)
                else:
                    row += '$'

            row += "   " + ', '.join(map(lambda com: com.name + '(' + str(com.hit_points) + ")", fighters))
            print(row)

    node_map: List[List[Node]] = []

    elves = []
    goblins = []
    all_combatants = []

    x = 0
    y = 0
    for line in file.read().split('\n'):
        node_map.append([])
        for char in line:
            new_node = None
            if char != '#':
                new_node = Node(x, y)

            if char in ('G', 'E'):
                c = Combatant(new_node, char + str(len(all_combatants)), debug)
                new_node.combatant = c
                all_combatants.append(c)
                if char == 'G':
                    goblins.append(c)
                else:
                    c.attack_points = elf_attack_points
                    elves.append(c)

            node_map[y].append(new_node)

            if new_node is not None:
                if x > 0 and node_map[y][x - 1] is not None:
                    Node.link_neighbors(new_node, node_map[y][x - 1])

                if y > 0 and node_map[y - 1][x] is not None:
                    Node.link_neighbors(new_node, node_map[y - 1][x])

            x += 1
        y += 1
        x = 0

    for l in node_map:
        for n in l:
            if n is not None:
                n.neighbors.sort()

    num_rounds = 0
    try:
        while len(elves) > 0 and len(goblins) > 0:
            start_time = datetime.now()
            someone_moved = False
            all_combatants.sort(key=cmp_to_key(Combatant.turn_order))
            dead_combatants = set()

            if debug:
                print('**********')
                # for c in all_combatants:
                #     print(str(c) + ' has ' + str(c.hit_points) + ' remaining hit points')

                print()
                print_map()
                print()
                print('********** Starting round ' + str(num_rounds + 1))

            for c in all_combatants:
                if c in dead_combatants:
                    continue

                enemies = elves if c in goblins else goblins

                if len(enemies) == 0:
                    raise StopIteration()

                ready_to_attack = False

                # check if an enemy is neighboring this combatant
                for neighbor in c.node.neighbors:
                    if neighbor.combatant in enemies:
                        ready_to_attack = True
                        break

                if not ready_to_attack:
                    # Find the shortest path to an enemy
                    paths = []
                    visited_nodes = set()
                    for neighbor in c.node.neighbors:
                        if neighbor.combatant is None:
                            first = Path(neighbor, 1, neighbor)
                            heapq.heappush(paths, first)
                            visited_nodes.add(neighbor)
                    visited_nodes.add(c.node)

                    found_path = None

                    while len(paths) > 0 and found_path is None:
                        p = heapq.heappop(paths)
                        new_paths: List[Path] = p.path_to_neighbors()
                        for new in new_paths:
                            node = new.get_endpoint()
                            if node in visited_nodes:
                                continue

                            if node.combatant is not None:
                                if node.combatant in enemies:
                                    found_path = new
                                else:
                                    visited_nodes.add(node)
                                    continue
                            else:
                                paths.append(new)
                                visited_nodes.add(node)

                    # found_path.sort()

                    if found_path is not None:
                        # Move to the first node in the path
                        new_pos = c.move(found_path)
                        for neighbor in new_pos.neighbors:
                            if neighbor.combatant in enemies:
                                ready_to_attack = True
                                break

                        someone_moved = True

                if ready_to_attack:
                    targets = []
                    for neighbor in c.node.neighbors:
                        if neighbor.combatant is not None and neighbor.combatant in enemies:
                            targets.append(neighbor.combatant)

                    targets.sort(key=cmp_to_key(Combatant.attack_order))

                    if(len(targets)) > 0:
                        e: Combatant = targets[0]
                        dead = c.attack(e)
                        if dead:
                            e.node.combatant = None
                            enemies.remove(e)
                            dead_combatants.add(e)
                            if e.attack_points > 3:
                                print(str(e) + ' dies')

            num_rounds += 1
            for d in dead_combatants:
                all_combatants.remove(d)
            if not someone_moved and debug:
                print('No one moved in round ', num_rounds)
            if debug:
                print(datetime.now() - start_time)

    finally:
        # no need to do anything here

        # print("num_rounds = " + str(num_rounds))
        remaining_points = 0
        for c in all_combatants:
            # print(c.name, c.hit_points)
            remaining_points += c.hit_points
        # print("remaining hit points = " + str(remaining_points))
        print(("Goblins" if len(goblins) > 0 else "Elves"), " win!")
        return num_rounds * remaining_points


# 29106 is too low

debug = False
# print(combat("reddit_1.txt", debug))
# print(combat("reddit_2.txt", debug))
# print(combat("reddit_3.txt", debug))
# assert(combat("example1.txt", debug) == 27730)
# assert(combat("example2.txt", debug) == 36334)
# assert(combat("example3.txt", debug) == 39514)
# assert(combat("example4.txt", debug) == 27755)
# assert(combat("example5.txt", debug) == 28944)
# assert(combat("example6.txt", debug) == 18740)
print("Part 1: ", combat("input.txt", debug))

# Part 2

# Attack Points   |  Winner
# --------------------------
#             4   |  Goblins
# combat("input.txt", debug, elf_attack_points=4)
#             8   |  Goblins
# combat("input.txt", debug, elf_attack_points=8)
#             16  | Elves
# combat("input.txt", debug, elf_attack_points=16)
#             32  | Elves
# combat("input.txt", debug, elf_attack_points=32)
#             24  | Elves
# combat("input.txt", debug, elf_attack_points=24)
#             20  | Elves
# combat("input.txt", debug, elf_attack_points=20)
#             18  | Elves
# combat("input.txt", debug, elf_attack_points=18)
#             19  | Elves
# combat("input.txt", debug, elf_attack_points=19)
#             20  | Elves
print("Part 2: ", combat("input.txt", debug, elf_attack_points=20))
