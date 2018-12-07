# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 07:31:53 2018

@author: Nino
"""

import numpy as np

fname = 'input.txt'

with open(fname) as f:
    lines = f.read().splitlines()

# get instructions
after = {}
all_steps = set()
for line in lines:
    a, b = line[5], line[36]
    all_steps.update([a, b])
    if b in after:
        after[b].append(a)
    else:
        after[b] = [a]

# add missing letters
all_steps = sorted(list(all_steps))
for step in all_steps:
    if step not in after:
        after[step]=[]


def first_part(req):
    done = []
    while req:
        potential_next_step = []
        for key in req:
            if set(req[key]).issubset(done):
                potential_next_step.append(key)
        next_step = sorted(potential_next_step)[0]
        done.append(next_step)
        req.pop(next_step)
    return(done)


done = first_part(after.copy())
print('solution to the first part (compact way):', ''.join(done))


def second_part(req, workers=5, max_duration=1000):
    timetable = np.zeros((max_duration, max_duration))
    in_progres = np.zeros(workers)
    processing = set()
    done = []
    worker = 0

    for t in range(max_duration):

        if not req and not in_progres.any():
            break

        potential_next_step = []
        for key in req:
            if set(req[key]).issubset(done):
                potential_next_step.append(key)

        for worker in range(workers):

            if not in_progres[worker]:
                if potential_next_step:
                    letter = sorted(potential_next_step)[0]
                    processing.add(letter)
                    req.pop(letter)
                    seconds = ord(letter) - 4
                    timetable[t, worker] = seconds
                    in_progres[worker] = True
                    potential_next_step.remove(letter)
            else:
                seconds = timetable[t-1, worker]
                letter = chr(int(seconds) + 4)
                timetable[t, worker] = seconds

            if (timetable[:, worker] == seconds).sum() == seconds:
                in_progres[worker] = False
                processing.remove(letter)
                done.append(letter)

    return timetable, done

_, done = second_part(after.copy(), workers=1, max_duration=3000)
print('solution to the first part (the hard way way):', ''.join(done))
timetable, done = second_part(after.copy(), workers=5, max_duration=1500)
print('solution to the second part:',
      str(np.where(timetable[:, 0] > 0)[0][-1]+1))
