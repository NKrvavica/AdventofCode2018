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

all_coord = []
claims = {}
for line in lines:

    # parse instructions
    line_nr, rest = line.split(' @ ')
    start, rectangle = rest.split(': ')
    x, y = map(int, start.split(','))
    rec_x, rec_y = map(int, rectangle.split('x'))

    # generate all coordinates per claim
    coordinates = list(itertools.product(x + np.array(range(rec_x)),
                                         y + np.array(range(rec_y))))
    all_coord.extend(coordinates)

    # generate dictionary (key - claims number, values - coordinates)
    claims[line_nr] = coordinates

# make 2D array and insert all claims
fabric = np.zeros((1000, 1000))
for x, y in all_coord:
    fabric[x, y] += 1

# results to the first part
print(len(fabric[fabric > 1]))

# results to the second part
for claim_id, coord in claims.items():
    overlap = False
    for x, y in coord:
        if fabric[x, y] != 1:
            overlap = True
            break
    if not overlap:
        print(claim_id)
        break

