# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 08:21:00 2018

Solution to day 1 for Advent of Code 2018.

@author: Nino
"""

import itertools

fname = 'input01.txt'

with open(fname) as f:
    lines = f.readlines()


def first_part(lines):
    """
    Modifies the starting frequency by series of
    positive or negative frequency changes

    Parameters
    ----------
    lines : list of strings
            Frequency changes given by some sign and number

    Returns
    -------
    frequency : int
                Resulting frequency after applying all changes
    """
    frequency = 0
    for value in lines:
        change = int(value.rstrip('\n'))
        frequency += change
    return(frequency)


solution1 = first_part(lines)
print('final frequency:', solution1)


def second_part(lines):
    """
    Modifies the starting frequency by series of
    positive or negative frequency changes and searches for the first
    occuranace when the resulting frequency repeates it self.

    Parameters
    ----------
    lines : list of strings
            Frequency changes given by some sign and number

    Returns
    -------
    frequency : int
                Frequency which is first repeated
    """
    list_of_freq = set()
    frequency = 0
    for value in itertools.cycle(lines):
        change = int(value.rstrip('\n'))
        frequency += change
        if frequency in list_of_freq:
            return frequency
        else:
            list_of_freq.add(frequency)


solution2 = second_part(lines)
print('repeated frequency:', solution2)
