from typing import List, Set

p1_deck_file = open("p1_deck.txt")
# p1_deck_file = open("p1_test.txt")
p1_deck_lines = p1_deck_file.read().splitlines()

p2_deck_file = open("p2_deck.txt")
# p2_deck_file = open("p2_test.txt")
p2_deck_lines = p2_deck_file.read().splitlines()

p1_deck = list(map(lambda n: int(n), p1_deck_lines))
p2_deck = list(map(lambda n: int(n), p2_deck_lines))


class GameState(object):

    def __init__(self, p1_deck: List[int], p2_deck: List[int]):
        self.p1_deck = p1_deck
        self.p2_deck = p2_deck

    def __eq__(self, o) -> bool:
        return self.p1_deck == o.p1_deck and self.p2_deck == o.p2_deck

    def __hash__(self):
        return hash((str(self.p1_deck), str(self.p2_deck)))


class Game(object):

    def __init__(self, p1_deck: List[int], p2_deck: List[int]):
        self.p1_deck = p1_deck
        self.p2_deck = p2_deck
        self.previous_states: Set[GameState] = set()

    def turn(self) -> int:
        state = GameState(self.p1_deck, self.p2_deck)
        if state in self.previous_states:
            return 1
        else:
            self.previous_states.add(state)

        p1_card = self.p1_deck.pop(0)
        p2_card = self.p2_deck.pop(0)

        if p1_card > len(self.p1_deck) or p2_card > len(self.p2_deck):
            p1_wins = (p1_card > p2_card)
        else:
            sub_game = Game(self.p1_deck[:p1_card].copy(), self.p2_deck[:p2_card].copy())
            p1_wins = (sub_game.play() == 1)

        if p1_wins:
            self.p1_deck.append(p1_card)
            self.p1_deck.append(p2_card)
        else:
            self.p2_deck.append(p2_card)
            self.p2_deck.append(p1_card)

        if len(self.p1_deck) == 0:
            return 2
        elif len(self.p2_deck) == 0:
            return 1
        else:
            return 0

    def play(self) -> int:
        winner = 0
        while winner == 0:
            winner = self.turn()
        return winner


game = Game(p1_deck, p2_deck)
score = 0
winner = game.play()
deck = game.p1_deck if winner == 1 else game.p2_deck
card_count = len(deck)

for i in range(card_count):
    score += deck[i] * (card_count - i)

print(score)
