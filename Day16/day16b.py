# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 09:27:54 2018

@author: Nino
"""


import re
import numpy as np

fname = 'input.txt'


def parse_input(fname):
    with open(fname) as f:
        lines = f.read().splitlines()
        befores = []
        afters = []
        instructions = []
        test_list = []
        empty_lines = False
        first_part = True
        for n, line in enumerate(lines):
            if first_part:
                if line[:6] == 'Before':
                    info = re.findall(r'\d+', line)
                    befores.append((list(map(int, info))))
                    empty_lines = False
                elif line[:5] == 'After':
                    info = re.findall(r'\d+', line)
                    afters.append((list(map(int, info))))
                elif line:
                    instructions.append((list(map(int, line.split(' ')))))
                else:
                    if empty_lines:
                        first_part = False
                    empty_lines = True
            else:
                if line != '':
                    test_list.append((list(map(int, line.split(' ')))))
        return befores, afters, instructions, test_list


def addr(register, a, b):
    return register[a] + register[b]

def addi(register, a, b):
    return register[a] + b

def mulr(register, a, b):
    return register[a] * register[b]

def muli(register, a, b):
    return register[a] * b

def banr(register, a, b):
    return register[a] & register[b]

def bani(register, a, b):
    return register[a] & b

def borr(register, a, b):
    return register[a] | register[b]

def bori(register, a, b):
    return register[a] | b

def setr(register, a, b):
    return register[a]

def seti(register, a, b):
    return a

def gtir(register, a, b):
    return a > register[b]

def gtri(register, a, b):
    return register[a] > b

def gtrr(register, a, b):
    return register[a] > register[b]

def eqir(register, a, b):
    return a == register[b]

def eqri(register, a, b):
    return register[a] == b

def eqrr(register, a, b):
    return register[a] == register[b]


# First part

def count_cases(operators, instructions, befores, afters):
    count = 0
    possibles = np.ones((16, 16), dtype=bool)
    for instruction, before, after in zip(instructions, befores, afters):
        a = instruction[1]
        b = instruction[2]
        c = np.zeros(16)
        for n, func in enumerate(operators):
            c[n] = func(before, a, b)
        check = (c == after[instruction[3]])
        if check.sum() >= 3:
            count += 1
        code = instruction[0]
        possibles[code, :] = np.logical_and(possibles[code, :], check)
    return count, possibles


operators = [addr, addi, mulr, muli, banr, bani, borr, bori,
             setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
befores, afters, instructions, test_list = parse_input(fname)
count, possibles = count_cases(operators, instructions, befores, afters)
print('solution to the first part:', count)


# Second part

def pair_numbers_with_operators(possibles):
    op_codes = {}
    while possibles.any():
        operator = np.argmax(possibles.sum(axis=0) == 1)
        number = np.argmax(possibles[:, operator] == 1)
        op_codes[number] = operators[operator]
        possibles[:, operator], possibles[number, :] = 0, 0
    return op_codes


def run_tests(test_list):
    op_codes = pair_numbers_with_operators(possibles)
    register = [0] * 4
    for test in test_list:
        nr, a, b, c = test
        operator = op_codes[nr]
        register[c] = operator(register, a, b)
    return register


register = run_tests(test_list)
print('solution to the second part:', register[0])
