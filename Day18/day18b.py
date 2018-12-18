# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:38:29 2018

@author: PC-KRVAVICA
"""

import numpy as np
import scipy.signal

fname = 'input.txt'
N = 50


def parse_input(fname, N, T):
    conversion = {'.': 0, '#': 1, '|': 2}
    with open(fname) as f:
        lines = f.read().splitlines()
        initial = np.zeros((N, N))
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                initial[i, j] = conversion[char]
    collection_area = np.zeros((T + 1, N + 2, N + 2))
    collection_area[0, 1: -1, 1: -1] = initial
    return collection_area


def iterate_in_time(collection_area, T):
    filter_adjecent = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    for t in range(1, T+1):
        field = collection_area[t - 1, 1: -1, 1: -1]
        adj_trees = scipy.signal.convolve2d(field == 2, filter_adjecent,
                                            mode='same')
        adj_lumber = scipy.signal.convolve2d(field == 1, filter_adjecent,
                                             mode='same')
        open_mask = field == 0
        lumber_mask = field == 1
        tree_mask = field == 2
        field[np.where(np.logical_and(open_mask, adj_trees >= 3))] = 2
        field[np.logical_and(tree_mask, adj_lumber >= 3)] = 1
        field[np.logical_and(lumber_mask,
                             np.logical_or(adj_trees < 1, adj_lumber < 1))] = 0
        collection_area[t, 1: -1, 1: -1] = field
    return collection_area


# First part
T = 10
collection_area = parse_input(fname, N, T)
collection_area = iterate_in_time(collection_area, T)
final_area = collection_area[T, 1: -1, 1: -1]
print((final_area == 2).sum().sum() * (final_area == 1).sum().sum())

# Second part
T = 1000
collection_area = parse_input(fname, N, T)
collection_area = iterate_in_time(collection_area, T)
final_area = collection_area[T, 1: -1, 1: -1]
print((final_area == 2).sum().sum() * (final_area == 1).sum().sum())
