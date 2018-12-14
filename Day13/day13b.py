# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 07:47:12 2018

@author: Nino
"""

import pandas as pd
import numpy as np


fname = 'input.txt'

with open(fname) as f:
    lines = f.read().splitlines()
    mapa = []
    for line in lines:
        mapa.append(list(line))

current_track = pd.DataFrame(mapa)

carts = {'<', '>', 'v', '^'}

cart_locations = np.array(current_track[current_track.isin(carts)].stack().
                          index.tolist())
cart_orientations = current_track[current_track.isin(carts)].stack().tolist()
cart_interesction = np.zeros(len(cart_locations))  # 0=L, 1=S, 2=R

# reconstruct the original map (without carts)
track = current_track.copy()
track.replace('<', '-', inplace=True)
track.replace('>', '-', inplace=True)
track.replace('v', '|', inplace=True)
track.replace('^', '|', inplace=True)


def sort_list(a, idx):
    b = []
    for i in idx:
        b.append(a[i])
    return b


def find_crashes(track, carts, cart_interesction, cart_locations,
                 cart_orientations, first_part):
    t = 0
    while True:
        t += 1
        carts_to_remove = set()
        for n, (loc, ori, inter) in enumerate(zip(cart_locations,
                                                  cart_orientations,
                                                  cart_interesction)):
            if ori == '<':
                if track.iloc[loc[0], loc[1]] == '-':
                    cart_locations[n, 1] -= 1
                elif track.iloc[loc[0], loc[1]] == '/':
                    cart_locations[n, 0] += 1
                    cart_orientations[n] = 'v'
                elif track.iloc[loc[0], loc[1]] == '\\':
                    cart_locations[n, 0] -= 1
                    cart_orientations[n] = '^'
                elif track.iloc[loc[0], loc[1]] == '+':
                    if inter == 0:
                        cart_locations[n, 0] += 1
                        cart_orientations[n] = 'v'
                        cart_interesction[n] = (cart_interesction[n] + 1) % 3
                    elif inter == 1:
                        cart_locations[n, 1] -= 1
                        cart_interesction[n] = (cart_interesction[n] + 1) % 3
                    elif inter == 2:
                        cart_locations[n, 0] -= 1
                        cart_orientations[n] = '^'
                        cart_interesction[n] = (cart_interesction[n] + 1) % 3

            elif ori == '>':
                if track.iloc[loc[0], loc[1]] == '-':
                    cart_locations[n, 1] += 1
                elif track.iloc[loc[0], loc[1]] == '/':
                    cart_locations[n, 0] -= 1
                    cart_orientations[n] = '^'
                elif track.iloc[loc[0], loc[1]] == '\\':
                    cart_locations[n, 0] += 1
                    cart_orientations[n] = 'v'
                elif track.iloc[loc[0], loc[1]] == '+':
                    if inter == 0:
                        cart_locations[n, 0] -= 1
                        cart_orientations[n] = '^'
                        cart_interesction[n] = (cart_interesction[n] + 1) % 3
                    elif inter == 1:
                        cart_locations[n, 1] += 1
                        cart_interesction[n] = (cart_interesction[n] + 1) % 3
                    elif inter == 2:
                        cart_locations[n, 0] += 1
                        cart_orientations[n] = 'v'
                        cart_interesction[n] = (cart_interesction[n] + 1) % 3

            elif ori == 'v':
                if track.iloc[loc[0], loc[1]] == '|':
                    cart_locations[n, 0] += 1
                elif track.iloc[loc[0], loc[1]] == '/':
                    cart_locations[n, 1] -= 1
                    cart_orientations[n] = '<'
                elif track.iloc[loc[0], loc[1]] == '\\':
                    cart_locations[n, 1] += 1
                    cart_orientations[n] = '>'
                elif track.iloc[loc[0], loc[1]] == '+':
                    if inter == 0:
                        cart_locations[n, 1] += 1
                        cart_orientations[n] = '>'
                        cart_interesction[n] = (cart_interesction[n] + 1) % 3
                    elif inter == 1:
                        cart_locations[n, 0] += 1
                        cart_interesction[n] = (cart_interesction[n] + 1) % 3
                    elif inter == 2:
                        cart_locations[n, 1] -= 1
                        cart_orientations[n] = '<'
                        cart_interesction[n] = (cart_interesction[n] + 1) % 3

            elif ori == '^':
                if track.iloc[loc[0], loc[1]] == '|':
                    cart_locations[n, 0] -= 1
                elif track.iloc[loc[0], loc[1]] == '/':
                    cart_locations[n, 1] += 1
                    cart_orientations[n] = '>'
                elif track.iloc[loc[0], loc[1]] == '\\':
                    cart_locations[n, 1] -= 1
                    cart_orientations[n] = '<'
                elif track.iloc[loc[0], loc[1]] == '+':
                    if inter == 0:
                        cart_locations[n, 1] -= 1
                        cart_orientations[n] = '<'
                        cart_interesction[n] = (cart_interesction[n] + 1) % 3
                    elif inter == 1:
                        cart_locations[n, 0] -= 1
                        cart_interesction[n] = (cart_interesction[n] + 1) % 3
                    elif inter == 2:
                        cart_locations[n, 1] += 1
                        cart_orientations[n] = '>'
                        cart_interesction[n] = (cart_interesction[n] + 1) % 3

            # detect crashes
            unq, count = np.unique(cart_locations, axis=0, return_counts=True)
            duplicates = unq[count > 1]
            if duplicates.any():
                if first_part:
                    return n, cart_locations
                else:
                    for d in duplicates:
                        carts_to_remove.add(np.where((d == cart_locations)
                                                     .sum(axis=1) > 1)[0][0])
                        carts_to_remove.add(np.where((d == cart_locations)
                                                     .sum(axis=1) > 1)[0][1])

        # remove carts that have crashed
        if carts_to_remove:
            for remove in sorted(list(carts_to_remove), reverse=True):
                cart_locations = np.delete(cart_locations, remove, axis=0)
                cart_interesction = np.delete(cart_interesction, remove,
                                              axis=0)
                cart_orientations.pop(remove)
            if len(cart_interesction) == 1:
                return cart_locations

        # sort carts (first by column, then by row)
        idx = np.lexsort(cart_locations[:, ::-1].T)
        cart_locations = cart_locations[idx]
        cart_orientations = sort_list(cart_orientations, idx)
        cart_interesction = cart_interesction[idx]


n, final_locations = find_crashes(track, carts, cart_interesction.copy(),
                                  cart_locations.copy(),
                                  cart_orientations.copy(), True)

print('solution:', final_locations[n][1], final_locations[n][0])

cart_locations = find_crashes(track, carts, cart_interesction,
                              cart_locations, cart_orientations, False)

print('solution:', cart_locations[0][1], cart_locations[0][0])
