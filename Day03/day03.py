# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 19:08:14 2018

@author: Nino
"""

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

        # # fill fabric with ones as instructed in the claim
        fabric[x:x+rec_x, y:y+rec_y] += 1

        # generate dictionary (key: claim number, values: coordinates)
        claims[line_nr] = np.array([[x, x+rec_x],
                                   [y, y+rec_y]])

    return fabric, claims


fabric, claims = cut_fabric(lines)

# results to the first part
print(len(fabric[fabric > 1]))


# results to the second part
def second_part(claims):
    for claim_id, coord in claims.items():
        if (fabric[coord[0, 0]:coord[0, 1],
                   coord[1, 0]:coord[1, 1]] == 1).all():
            return claim_id


print(second_part(claims))
