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
    rot1, rot2 = -2, +7

    for i in range(1, last_marble + 1):
        current_elf = next(elfs)
        if i % 23 == 0:
            marble_list.rotate(rot2)
            take_marble = marble_list.popleft()
            score[current_elf] += i + take_marble
        else:
            marble_list.rotate(rot1)
            marble_list.appendleft(i)

    return score


# First part
score = play(players=428, last_marble=72061)
print('max. score:', max(score))

# Second part
score = play(players=428, last_marble=7206100)
print('max. score:', max(score))
