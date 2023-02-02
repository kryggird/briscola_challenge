#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from example_ai import RandomAI
from my_ai import HeuristicAI
from simulator import play_many

if __name__ == "__main__":
    a1, a2 = HeuristicAI(), RandomAI()
    
    print(play_many(a1, a2))
