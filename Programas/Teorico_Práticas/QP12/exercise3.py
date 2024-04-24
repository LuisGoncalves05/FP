import random
from typing import List, Tuple

# card suits
SUITS = "♠ ♡ ♢ ♣".split()  # spade, heart, diamond, club
# card ranks
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()  # 2-10, Jack, Queen, King, Ace

Card = Tuple[str, str]
Deck = List[Card]

def create_deck(shuffle: bool = False) -> Deck:
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck

def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])

def choose(items):
    """Choose and return a random item"""
    return random.choice(items)

def player_order(names, start=None):
    """Rotate player order so that start goes first"""
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]

def card_value(card):
    if card[0] in "♠♣":
        mult = 2
    else:
        mult = 1
    if card[1] == "A":
        return 11*mult
    elif card[1] in "JQK":
        return 10*mult
    else:
        return int(card[1])*mult

def play(seed_value) -> None:
    random.seed(seed_value)
    deck = create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}
    start_player = choose(names)
    turn_order = player_order(names, start=start_player)
    points = [0]*4
    while hands[start_player]:
        play = []
        for name in turn_order:
            card = choose(hands[name])
            hands[name].remove(card)
            play.append(card_value(card))
        m1 = max(play)
        maxes1 = []
        for i, point in enumerate(play):
            if point == m1:
                maxes1.append(i)
        for item in maxes1:
            points[item] +=1
    m2 = max(points)
    maxes2 = []
    for i, point in enumerate(points):
        if point == m2:
            maxes2.append(turn_order[i])
    maxes2.sort()
    return " ".join(maxes2)

if __name__ == "__main__":
    print(play(999))
    print(play(31))
    print(play(72))
    print(play(19))