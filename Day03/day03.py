# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 19:08:14 2018

@author: Nino
"""

import numpy as np

fname = 'input.txt'

with open(fname) as f:
    lines = f.read().splitlines()


def parse_input(line):
    claim_id, rest = line.split(' @ ')
    start, rectangle = rest.split(': ')
    x, y = map(int, start.split(','))
    h, w = map(int, rectangle.split('x'))
    return claim_id, x, y, h, w


def cut_fabric(lines, N=1000):
    claims = {}
    fabric = np.zeros((N, N))
    for line in lines:
        claim_id, x, y, h, w = parse_input(line)
        fabric[x:x+h, y:y+w] += 1
        claims[claim_id] = np.array([[x, x+h],
                                     [y, y+w]])
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
