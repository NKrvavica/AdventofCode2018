# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 07:14:34 2018

@author: Nino
"""

import re
import numpy as np
import matplotlib.pyplot as plt

fname = 'input.txt'

with open(fname) as f:
    lines = f.read().splitlines()
    positions = np.zeros((len(lines), 2))
    velocities = np.zeros((len(lines), 2))
    for n, line in enumerate(lines):
        info = re.findall('<.*?>', line)
        positions[n, :] = (list(map(int, info[0][1:-1].split(','))))
        velocities[n, :] = (list(map(int, info[1][1:-1].split(','))))


def get_message(positions, velocities):
    t = 0
    min_dy = positions[:, 1].max() - positions[:, 1].min()
    while True:
        t += 1
        positions += velocities
        dy = positions[:, 1].max() - positions[:, 1].min()
        if dy < min_dy:
            min_dy = dy
        else:
            positions -= velocities
            return t-1, positions


t, positions = get_message(positions, velocities)
print('seconds:', t)

plt.figure()
plt.scatter(positions[:, 0], -positions[:, 1])
plt.axis('equal')

