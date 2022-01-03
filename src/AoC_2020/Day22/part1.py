p1_deck_file = open("p1_deck.txt")
# p1_deck_file = open("p1_test.txt")
p1_deck_lines = p1_deck_file.read().splitlines()

p2_deck_file = open("p2_deck.txt")
# p2_deck_file = open("p2_test.txt")
p2_deck_lines = p2_deck_file.read().splitlines()

p1_deck = list(map(lambda n: int(n), p1_deck_lines))
p2_deck = list(map(lambda n: int(n), p2_deck_lines))

while len(p1_deck) > 0 and len(p2_deck) > 0:
    p1_card = p1_deck.pop(0)
    p2_card = p2_deck.pop(0)

    if p1_card > p2_card:
        p1_deck.append(p1_card)
        p1_deck.append(p2_card)
    else:
        p2_deck.append(p2_card)
        p2_deck.append(p1_card)

winning_deck = p1_deck if len(p1_deck) > 0 else p2_deck
score = 0
card_count = len(winning_deck)
for i in range(card_count):
    score += winning_deck[i] * (card_count - i)

print(score)