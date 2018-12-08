# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 08:12:42 2018

Solution to day 2 for Advent of Code 2018.

@author: Nino
"""

import itertools
from collections import Counter

fname = 'input.txt'

with open(fname) as f:
    lines = f.read().splitlines()


def first_part(lines):
    double_letters = 0
    tripple_letters = 0
    for line in lines:
        count = Counter()
        for s in line:
            count[s] += 1
        if 2 in count.values():
            double_letters += 1
        if 3 in count.values():
            tripple_letters += 1
    return double_letters * tripple_letters


print('checksum: ', first_part(lines))


def second_part(lines):

    def match(s1, s2):
        """ Checks if two string differ by exactly one character"""
        count_diffs = 0
        for i, (a, b) in enumerate(zip(s1, s2)):
            if a != b:
                if count_diffs:
                    return -1
                count_diffs += 1
        return i

    """ Compare each string to every other in the list,
    using itertools.combinations"""
    for line1, line2 in itertools.combinations(lines, 2):
        check = match(line1, line2)
        if check >= 0:
            return line1[:check] + line1[check+1:]


print('common letters:', second_part(lines))
