import re

DECK_SIZE = 10007

filename = "input.txt"
# filename = "test1.txt"
# filename = "test2.txt"
# filename = "test3.txt"
# filename = "test4.txt"
file = open(filename)
input_lines = file.read().splitlines()

deck = [x for x in range(0, DECK_SIZE)]

print(deck)


def cut(x):
    # print("Cut the deck with " + str(x) + " cards")
    global deck
    top = deck[x:]
    bottom = deck[:x]
    deck = top
    deck.extend(bottom)


def new_stack():
    # print("dealing new stack")
    global deck
    deck.reverse()


def increment(x):
    global deck
    new_deck = [None] * DECK_SIZE
    for i in range(0, DECK_SIZE):
        new_deck[(i * x) % DECK_SIZE] = deck[i]

    deck = new_deck


for line in input_lines:
    m = re.search("cut (.*)", line)
    if m:
        cut(int(m.group(1)))
        continue

    m = re.search("deal into new stack", line)
    if m:
        new_stack()
        continue

    m = re.search("deal with increment (.*)", line)
    if m:
        increment(int(m.group(1)))
        continue

print(deck)
for i in range(0, DECK_SIZE):
    if deck[i] == 2019:
        print(i)