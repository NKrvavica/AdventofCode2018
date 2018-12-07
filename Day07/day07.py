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
        after[step] = []


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


def second_part(req, workers=1, max_duration=10_000):
    timetable = np.zeros((max_duration, max_duration))
    in_progres = np.zeros(workers)
    seconds = np.zeros(workers)
    letter = [''] * workers
    done = set()
    solution = []
    worker, t = 0, 0
    while req or in_progres.any():

        # generate a list of available jobs
        potential_next_step = []
        for key in req:
            if set(req[key]).issubset(done):
                potential_next_step.append(key)

        for worker in range(workers):
        # if work is in progress, continue in the current time step
            if in_progres[worker]:
                timetable[t, worker] = seconds[worker]
                in_progres[worker] += 1
        # if work is not in progress, but some jobs are waiting, start them
            elif potential_next_step:
                letter[worker] = sorted(potential_next_step)[0]
                seconds[worker] = ord(letter[worker]) - 4 # A = 61
                timetable[t, worker] = seconds[worker]
                in_progres[worker] = 1
                req.pop(letter[worker])
                potential_next_step.remove(letter[worker])

        # check if the job at the current time step is finished
            if in_progres[worker] == seconds[worker]:
                in_progres[worker] = 0
                done.add(letter[worker])
                solution.append(letter[worker])

        t += 1

    return timetable, solution


_, solution = second_part(after.copy(), workers=1, max_duration=2000)
print('solution to the first part (the hard way way):', ''.join(done))

timetable, solution = second_part(after.copy(), workers=5, max_duration=1200)
print('solution to the second part:',
      str(np.where(timetable[:, 0] > 0)[0][-1]+1))
