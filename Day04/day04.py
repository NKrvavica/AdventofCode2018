# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 12:06:48 2018

@author: PC-KRVAVICA
"""

import re
import numpy as np
from datetime import datetime

fname = 'input.txt'

with open(fname) as f:
    lines = f.read().splitlines()


def fill_the_records(lines):
    sorted_input = sorted(lines)
    records = {}
    for instruc in sorted_input:
        if instruc[19:24] == 'Guard':
            guard_id = re.findall('\d+', instruc[25:])[0]
            if guard_id not in records.keys():
                records[guard_id] = np.zeros(60)
        elif instruc[19:24] == 'falls':
            date_time = datetime.strptime(instruc[1:17], '%Y-%m-%d %H:%M')
            starttime = date_time.minute
        elif instruc[19:24] == 'wakes':
            date_time = datetime.strptime(instruc[1:17], '%Y-%m-%d %H:%M')
            endtime = date_time.minute
            records[guard_id][starttime:endtime] += 1
    return records


records = fill_the_records(lines)


def first_part(records):
    """ which guard sleeps the most """
    max_sleep = 0
    for guard, sleep_time in records.items():
        if sleep_time.sum() > max_sleep:
            max_sleep = sleep_time.sum()
            sleepy_guard = guard
            minute = np.argmax(sleep_time)
    return int(sleepy_guard) * minute


answer1 = first_part(records)
print(answer1)


def second_part(records):
    """ which guard sleeps most frequently at the same time """
    max_frequency = 0
    for guard, sleep_time in records.items():
        if sleep_time.max() > max_frequency:
            max_frequency = sleep_time.max()
            sleepy_guard = guard
            minute = np.argmax(sleep_time)
    return int(sleepy_guard) * minute


answer2 = second_part(records)
print(answer2)
