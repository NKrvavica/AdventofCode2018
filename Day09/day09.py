# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 08:32:08 2018

@author: Nino
"""

from collections import deque
import itertools


def play(players, last_marble):

    marble_list = deque([0])
    elfs = itertools.cycle(range(players))
    score = [0] * players

    for i in range(1, last_marble + 1):
        current_elf = next(elfs)
        if i % 23 == 0:
            position = -7
            take_marble = marble_list[position]
            score[current_elf] += i + take_marble
            marble_list.rotate(-position)
            marble_list.popleft()
        else:
            marble_list.rotate(-2)
            marble_list.insert(0, i)

    return score


# First part
score = play(players=428, last_marble=72061)
print('max. score:', max(score))

# Second part
score = play(players=428, last_marble=7206100)
print('max. score:', max(score))
