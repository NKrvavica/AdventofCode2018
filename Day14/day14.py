# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 19:02:43 2018

@author: NinoK
"""


def first_part(recepies, pos, AFTER):
    while True:
        score = (recepies[pos[0]], recepies[pos[1]])
        suma = score[0] + score[1]
        digits = [int(x) for x in str(suma)]
        recepies.extend(digits)
        length = len(recepies)
        pos[0] = (pos[0] + score[0] + 1) % length
        pos[1] = (pos[1] + score[1] + 1) % length
        if length >= AFTER + 10:
            return recepies


recepies = [3, 7]
pos = [0, 1]
AFTER = 320851
results = first_part(recepies.copy(), pos.copy(), AFTER)
print(''.join( map(str, results[-10:])))


def second_part(recepies, pos, BEFORE):
    length = len(recepies)
    before_digits = [int(x) for x in BEFORE]
    len_before = len(before_digits)
    while True:
        score = (recepies[pos[0]], recepies[pos[1]])
        suma = score[0] + score[1]
        digits = list(str(suma))
        for d in digits:
            recepies.extend([int(d)])
            if recepies[-len_before:] == before_digits:
                return len(recepies) - len_before
        length += len(digits)
        pos[0] = (pos[0] + score[0] + 1) % length
        pos[1] = (pos[1] + score[1] + 1) % length


BEFORE = 320851
results = second_part(recepies, pos, str(BEFORE))
print(results)
