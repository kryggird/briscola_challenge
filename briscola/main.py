# -*- coding: utf-8 -*-
from collections import Counter

from .example_ai import RandomAI
from .simulator import play_many

def run_main():
    a1, a2 = RandomAI(), RandomAI()
   
    p1_scores = []
    print(play_many(a1, a2, runs=3000, callback=p1_scores.append))

    histogram = Counter(p1_scores)
    for score in sorted(histogram):
        print(f"{score:3d}: " + "#" * histogram[score])

if __name__ == "__main__":
    run_main()
