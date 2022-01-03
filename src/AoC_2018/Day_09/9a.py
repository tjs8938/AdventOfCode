#!/bin/python

NUM_PLAYERS = 464
NUM_MARBLES = 70918

player_scores = [0] * NUM_PLAYERS
marble_circle = [0]

next_marble = 1
current_index = 0
next_player = 1

while next_marble <= NUM_MARBLES:
    if next_marble % 23 == 0:
        player_scores[next_player - 1] += next_marble
        current_index = current_index - 7
        if current_index < 0:
            current_index += len(marble_circle)
        player_scores[next_player - 1] += marble_circle.pop(current_index)
    else:
        if current_index + 2 <= len(marble_circle):
            current_index += 2
        else:
            current_index = 1
        marble_circle.insert(current_index, next_marble)

    next_marble += 1
    next_player += 1
    if next_player > NUM_PLAYERS:
        next_player = 1

high_score = 0
for score in player_scores:
    if score > high_score:
        high_score = score

print (high_score)
