# -*- coding: utf-8 -*-

from .example_ai import RandomAI
from .simulator import play_many

def run_main():
    a1, a2 = RandomAI(), RandomAI()
    
    print(play_many(a1, a2))

if __name__ == "__main__":
    run_main()
