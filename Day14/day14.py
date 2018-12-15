# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 19:02:43 2018

@author: NinoK
"""

from numba import jit

INPUT = 320851
recepies = [3, 7]
pos = [0, 1]
before_digits = [int(x) for x in str(INPUT)]


def first_part(recepies, pos, INPUT):
    while True:
        score = (recepies[pos[0]], recepies[pos[1]])
        suma = score[0] + score[1]
        digits = [int(x) for x in str(suma)]
        recepies.extend(digits)
        length = len(recepies)
        pos[0] = (pos[0] + score[0] + 1) % length
        pos[1] = (pos[1] + score[1] + 1) % length
        if length >= INPUT + 10:
            return recepies


results = first_part(recepies.copy(), pos.copy(), INPUT)
print(''.join(map(str, results[-10:])))


@jit(nopython=True)
def second_part_faster(recepies, pos, before_digits, INPUT):
    length = len(recepies)
    len_before = len(before_digits)
    while True:
        score = (recepies[pos[0]], recepies[pos[1]])
        suma = score[0] + score[1]
        if suma < 10:
            length += 1
            recepies.append(suma)
            if recepies[-len_before:] == before_digits:
                return length - len_before
        else:
            length += 2
            recepies.append(1)
            if recepies[-len_before:] == before_digits:
                return length - 1 - len_before
            recepies.append(suma - 10)
            if recepies[-len_before:] == before_digits:
                return length - len_before
        pos[0] = (pos[0] + score[0] + 1) % length
        pos[1] = (pos[1] + score[1] + 1) % length


results = second_part_faster(recepies.copy(), pos.copy(), before_digits, INPUT)
print(results)
