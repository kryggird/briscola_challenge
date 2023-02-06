#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum, IntEnum, auto
from random import shuffle

class Rank(IntEnum):
    Two = auto()
    Four = auto()
    Five = auto()
    Six = auto()
    Seven = auto()
    Knave = auto()
    Knight = auto()
    King = auto()
    Three = auto()
    Ace = auto()

class Suit(Enum):
    Swords = auto()
    Cups = auto()
    Coin = auto()
    Batons = auto()

POINTS = {
    Rank.Ace: 11,
    Rank.Three: 10,
    Rank.Knave: 2,
    Rank.Knight: 3,
    Rank.King: 4,
}

class Card:
    def __init__(self, rank, suit, *, is_trump=False):
        self.rank = rank
        self.suit = suit
        self.is_trump = is_trump

    def __hash__(self):
        return hash((self.rank.value, self.suit.value))

    @property
    def points(self):
        return POINTS.get(self.rank, 0)
        
    def __repr__(self):
        suffix = "*" if self.is_trump else ""
        return f"Card({self.rank.name}, {self.suit.name}{suffix})"

# Biased toward `lhs`
def compare(lhs: Card, rhs: Card):
    if lhs.suit == rhs.suit:
        return lhs.rank >= rhs.rank
    elif rhs.is_trump:
        return False
    else:
        return True

class Player:
    def __init__(self, ai, deck, hand=None):
        self.ai = ai
        if hand is None:
            self.hand = [deck.pop(), deck.pop(), deck.pop()]
        else:
            self.hand = hand
        self.taken = []

    def play_first(self, other_taken: [Card], last_card: Card):
        idx = self.ai.play_first(self.hand, self.taken, other_taken, last_card)
        return self.hand.pop(idx)
    
    def play_second(self, played_card: Card, other_taken: [Card], last_card: Card):
        idx = self.ai.play_second(self.hand, self.taken, played_card, other_taken, last_card)
        return self.hand.pop(idx)


# Last card is 0. That way we can draw card with `pop`
def make_shuffled_deck():
    deck = [Card(r, s) for r in Rank for s in Suit]
    shuffle(deck)    
    for c in deck:
        c.is_trump = c.suit == deck[0].suit
    return deck

def play_once(player_1, player_2, deck):
    winner, loser = player_1, player_2
    
    while deck:
        card_1 = winner.play_first(loser.taken, deck[0])
        card_2 = loser.play_second(card_1, winner.taken, deck[0])
        
        # Player 2 takes, swap players for next round
        if not compare(card_1, card_2):
            winner, loser = loser, winner

        winner.taken.extend([card_1, card_2])
        if deck:
            winner.hand.append(deck.pop())
            loser.hand.append(deck.pop())

    score_1 = sum(t.points for t in player_1.taken)
    score_2 = sum(t.points for t in player_2.taken)

    return score_1, score_2

def play_many(ai_1, ai_2, runs=40000):
    count_1, count_2 = 0, 0
    for _ in range(runs // 2):
        deck = make_shuffled_deck()
        p1, p2 = Player(ai_1, deck), Player(ai_2, deck)
        s1, s2 = play_once(p1, p2, deck)
        count_1 += s1 > s2
        count_2 += s2 > s1
    
    for _ in range(runs // 2):
        deck = make_shuffled_deck()
        p1, p2 = Player(ai_1, deck), Player(ai_2, deck)
        s2, s1 = play_once(p2, p1, deck)
        count_1 += s1 > s2
        count_2 += s2 > s1

    return (count_1, count_2)
