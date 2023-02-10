#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC
from random import choice

from .simulator import compare, Rank, Suit, Card

class AbstractAI(ABC):
    def play_first(self, hand, taken, other_taken, last_card):
        ...
    
    def play_second(self, hand, taken, played_card, other_taken, last_card):
        ...
        
class RandomAI(AbstractAI):
    def play_first(self, hand, *args, **kwargs):
        return choice(range(len(hand)))
        
    def play_second(self, hand, *args, **kwargs):
        return choice(range(len(hand)))
