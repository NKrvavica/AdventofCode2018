# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 19:08:14 2018

@author: Nino
"""

import itertools
import numpy as np

fname = 'input.txt'

with open(fname) as f:
    lines = f.read().splitlines()

def cut_fabric(lines):

    claims = {}
    fabric = np.zeros((1000, 1000))

    for line in lines:

        # parse instructions
        line_nr, rest = line.split(' @ ')
        start, rectangle = rest.split(': ')
        x, y = map(int, start.split(','))
        rec_x, rec_y = map(int, rectangle.split('x'))

        # generate all coordinates per claim
        coordinates = list(itertools.product(x + np.arange(rec_x),
                                             y + np.arange(rec_y)))

        # fill fabric with ones as instructed in the claim
        for x, y in coordinates:
            fabric[x, y] += 1

        # generate dictionary (key - claims number, values - coordinates)
        claims[line_nr] = coordinates

    return fabric, claims

fabric, claims = cut_fabric(lines)

# results to the first part
print(len(fabric[fabric > 1]))

# results to the second part
def second_part(claims):
    for claim_id, coord in claims.items():
        overlap = False
        for x, y in coord:
            if fabric[x, y] != 1:
                overlap = True
                break
        if not overlap:
            return claim_id

print(second_part(claims))

