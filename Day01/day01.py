# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 08:21:00 2018

Solution to day 1 for Advent of Code 2018.

@author: Nino
"""

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
                Resulting frequency after applying all shanges
    """
    frequency = 0
    for value in lines:
        change = int(value.rstrip('\n'))
        frequency += change
    print('final frequency:', frequency)
    return(frequency)

solution1 = first_part(lines)

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
    list_of_freq =set()
    frequency = 0
    found_duplicate = False
    while not found_duplicate:
        for value in lines:
            change = int(value.rstrip('\n'))
            frequency += change
            if frequency in list_of_freq:
                print('repeated frequency:', frequency)
                found_duplicate=True
                break
            else:
                list_of_freq.add(frequency)
    return frequency

solution2 = second_part(lines)
