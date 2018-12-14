# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 08:48:06 2018

@author: Nino
"""

fname = 'input.txt'

with open(fname) as f:
    lines = f.read().splitlines()
    initial = lines[0].split(': ')[1]
    notes_tree = set()
    for note in lines[2:]:
        notes_pattern, notes_bool = (note.split(' => '))
        if notes_bool == '#':
            notes_tree.add(notes_pattern)


def predict_trees(initial, notes_tree, GEN):
    initial = '....' + initial + '....'
    pos = -4
    sums = []
    for t in range(GEN):
        if initial[:4] != '....':
            initial = '.' + initial
            pos -= 1
        if initial[-4:] != '....':
            initial = initial + '.'
        new = '..'
        for n, _ in enumerate(initial[:-3]):
            if initial[n:n+5] in notes_tree:
                new = new + '#'
            else:
                new = new + '.'
        new = new + '..'
        initial = new

        counter = 0
        for n, c in enumerate(new):
            if c == '#':
                counter += n + pos
        sums.append(counter)

    return sums


# First part
GEN1 = 20
sums = predict_trees(initial, notes_tree, GEN1)
print('solution:', sums[-1])

# Second part
GEN_temp = 200
sums = predict_trees(initial, notes_tree, GEN_temp)
rate = sums[-1] - sums[-2]
GEN2 = 50000000000
solution = (GEN2 - GEN_temp) * rate + sums[-1]
print('solution:', solution)
