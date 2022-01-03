#!/bin/python

NUM_PLAYERS = 464
NUM_MARBLES = 7091800`

player_scores = [0] * NUM_PLAYERS

next_marble = 2
next_player = 1


class Node:
    def __init__(self, next_node, previous_node, value):
        self.value = value
        self.next_node = next_node
        self.previous_node = previous_node


node_zero = Node(None, None, 0)
node_one = Node(node_zero, node_zero, 1)

node_zero.next_node = node_one
node_zero.previous_node = node_one

current_node = node_one

while next_marble <= NUM_MARBLES:
    if next_marble % 23 == 0:
        player_scores[next_player - 1] += next_marble

        count = 7
        while count > 0:
            current_node = current_node.previous_node
            count -= 1

        player_scores[next_player - 1] += current_node.value

        temp_node = current_node
        current_node.next_node.previous_node = current_node.previous_node
        current_node.previous_node.next_node = current_node.next_node
        current_node = current_node.next_node
        del temp_node
    else:

        prev = current_node.next_node
        next = prev.next_node

        current_node = Node(next, prev, next_marble)
        prev.next_node = current_node
        next.previous_node = current_node

    next_marble += 1
    next_player += 1
    if next_player > NUM_PLAYERS:
        next_player = 1

high_score = 0
for score in player_scores:
    if score > high_score:
        high_score = score

print(high_score)
