# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 08:12:42 2018

Solution to day 2 for Advent of Code 2018.

@author: Nino
"""

import itertools

fname = 'input.txt'

with open(fname) as f:
    lines = f.read().splitlines()

def first_part(lines):
    double_letters = 0
    tripple_letters = 0
    for line in lines:
        count = {}
        for s in line:
          if s in count:
            count[s] += 1
          else:
            count[s] = 1
        double_tripple = set(count.values())
        if 2 in double_tripple: double_letters += 1
        if 3 in double_tripple: tripple_letters += 1
    return double_letters * tripple_letters


print('checksum: ', first_part(lines))


def second_part(lines):

    def match(s1, s2):
        """ Checks if two string differ by exactly one character at the same
        position """
        l = [False, -1]
        for i in range(len(s1)):
            if s1[:i]==s2[:i] and s1[i]!=s2[i] and s1[i+1:]==s2[i+1:]:
                l = [True, i]
                break
        return l

    """ Compare each string to every other in the list,
    using itertools.combinations"""
    for line1, line2 in itertools.combinations(lines, 2):
        l = match(line1, line2)
        if l[0]:
            return line1[:l[1]] + line1[l[1]+1:]


print('common letters:', second_part(lines))
