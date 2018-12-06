# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 07:11:59 2018

@author: Nino
"""

import numpy as np

fname = 'input.txt'

with open(fname) as f:
    lines = f.read().splitlines()
    loc = []
    for n, line in enumerate(lines):
        loc.append(list(map(int, line.split(', '))))


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# @profile
def first_part(loc):

    max_coord = int(loc.max())
    grid = np.zeros((max_coord, max_coord))
    region_sizes = {}
    region_size = 0

    for ix in range(max_coord):
        for iy in range(max_coord):
            distance = manhattan(ix, iy, loc[:, 0], loc[:, 1])
            # first part
            closest = np.where(distance == distance.min())[0]
            region = closest[0]
            if len(closest) == 1:
                grid[ix, iy] = closest
                if region in region_sizes:
                    region_sizes[region] += 1
                else:
                    region_sizes[region] = 1
            else:
                grid[ix, iy] = np.nan
            if ix==0 or ix==max_coord-1 or iy==0 or iy==max_coord-1:
                region_sizes[region] = -999
            # second part
            if distance.sum() < 10_000:
                region_size += 1
    max_region_1 = region_sizes[max(region_sizes, key=region_sizes.get)]
    max_region_2 = region_size
    return max_region_1, max_region_2


a, b = first_part(np.array(loc))
print('solution to the first part:', a)
print('solution to the second part:', b)
