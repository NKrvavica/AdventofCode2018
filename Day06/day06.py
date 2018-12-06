# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 07:11:59 2018

@author: Nino
"""

import itertools
import numpy as np

fname = 'input.txt'
loc = np.loadtxt(fname, delimiter=',')


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def find_regions(loc):
    max_coord = int(loc.max())
    region_sizes = {}
    max_region_size = 0
    for ix, iy in itertools.product(range(max_coord), range(max_coord)):
        distance = manhattan(ix, iy, loc[:, 0], loc[:, 1])
        # first part
        first_idx, second_idx = distance.argsort()[0:2]
        if distance[first_idx] != distance[second_idx]:
            if first_idx in region_sizes:
                region_sizes[first_idx] += 1
            else:
                region_sizes[first_idx] = 1
        if ix==0 or ix==max_coord-1 or iy==0 or iy==max_coord-1:
            region_sizes[first_idx] = -999
        # second part
        if distance.sum() < 10_000:
            max_region_size += 1
    max_region_1 = region_sizes[max(region_sizes, key=region_sizes.get)]
    return max_region_1, max_region_size


a, b = find_regions(loc)
print('solution to the first part:', a)
print('solution to the second part:', b)
