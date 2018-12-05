# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 07:39:31 2018

@author: Nino
"""

import string
from numba import jit

fname = 'input.txt'

with open(fname) as f:
    polymer = f.read()

# generate a list of nits which react
reactants = [a+b for a, b in zip(string.ascii_lowercase,
                                 string.ascii_uppercase)]
reactants2 = [a+b for a, b in zip(string.ascii_uppercase,
                                  string.ascii_lowercase)]
reactants.extend(reactants2)


def react(polymer, reactants):
    reacting=True
    while reacting:
        reacting=False
        for combo in reactants:
            if combo in polymer:
                reacting=True
                polymer = polymer.replace(combo, '')
    return polymer


# first part
reacted_polymer = react(polymer, reactants)
print(len(reacted_polymer))


# second part
@jit
def second_part(polymer, problematics, reactants):
    shortest = len(polymer)
    for element in problematics:
        second_polymer = polymer.replace(element[0], '')
        second_polymer = second_polymer.replace(element[1], '')
        reacted_polymer = react(second_polymer, reactants)
        polymer_length = len(reacted_polymer)
        if polymer_length < shortest:
            shortest = polymer_length
    return shortest


shortest = second_part(polymer, reactants2, reactants)
print(shortest)
