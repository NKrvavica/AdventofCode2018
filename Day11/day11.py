# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 07:09:36 2018

@author: Nino
"""

import numpy as np
from numba import jit

# Input
SERIAL = 7672
N = 300


def get_digit(x, n):
    return np.remainder(np.floor_divide(x, 10**n), 10)


def comp_power_levels(N, serial):
    n = list(range(1, N+1))
    xc, yc = np.meshgrid(n, n)
    rackID = xc + 10
    almost_there = (rackID * yc + serial) * rackID
    return get_digit(almost_there, 2) - 5


power_level = comp_power_levels(N, SERIAL)


# First part
@jit(nopython=True)
def max_NxN_cell(power_level, size):
    max_power = 0
    for j in range(N - size):
        for i in range(N - size):
            fuel_cell_power = power_level[j:j+size, i:i+size].sum()
            if fuel_cell_power > max_power:
                max_power = fuel_cell_power
                max_power_coord = (i+1, j+1)
    return max_power_coord, max_power


max_power_coord, _ = max_NxN_cell(power_level, 3)
print(max_power_coord)


# Second part
def find_max_fuel_cell(power_level, N):
    max_power = 0
    for size in range(2, N):
        cell_coord, cell_power = max_NxN_cell(power_level, size)
        if cell_power > max_power:
            max_power = cell_power
            max_power_coord = (cell_coord, size)
    return max_power_coord


max_power_coord = find_max_fuel_cell(power_level, N)
print(max_power_coord)
