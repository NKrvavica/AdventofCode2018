# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 12:06:48 2018

@author: PC-KRVAVICA
"""

import re
import collections
import numpy as np
import pandas as pd
from datetime import datetime

fname = 'input.txt'

with open(fname) as f:
    lines = f.read().splitlines()


def sort_inputs(lines):
    unsorted_input = {}
    for n, line in enumerate(lines):
        pd_date = datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
        unsorted_input[pd_date] = line
    sorted_input = collections.OrderedDict(sorted(unsorted_input.items()))
    return sorted_input


sorted_input = sort_inputs(lines)


def fill_the_records(sorted_input):
    column_list = ['ID']
    column_list.extend(list(range(60)))
    records = pd.DataFrame(columns=column_list)
    indx = -1
    for date, instruc in sorted_input.items():
        if instruc[19:24] == 'Guard':
            indx += 1
            guard_id = re.findall('\d+', instruc[25:])[0]
            records.loc[indx, 'ID'] = int(guard_id)
        elif instruc[19:24] == 'falls':
            startime = date.minute
        elif instruc[19:24] == 'wakes':
            endtime = date.minute
            records.iloc[indx, startime+2:endtime+2] = 1
    records.fillna(0, inplace=True)
    return records


records = fill_the_records(sorted_input)


def first_part(records):
    """ which guard sleeps the most """
    max_sleep = 0
    for i in set(records['ID']):
        guard_records = records[records['ID'] == i].iloc[:, 2:]
        minute_at_sleep = guard_records.values.sum(axis=0)
        if minute_at_sleep.sum() > max_sleep:
            max_sleep = minute_at_sleep.sum()
            guard_id = i
            minute = np.argmax(minute_at_sleep)
    return guard_id * minute


answer1 = first_part(records)
print(answer1)


def second_part(records):
    """ which guard sleeps most frequently at the same time """
    max_frequency = 0
    for i in set(records['ID']):
        guard_records = records[records['ID'] == i].iloc[:, 2:]
        minute_at_sleep = guard_records.values.sum(axis=0)
        if minute_at_sleep.max() > max_frequency:
            max_frequency = minute_at_sleep.max()
            guard_id = i
            minute = np.argmax(minute_at_sleep)
    return guard_id * minute


answer2 = second_part(records)
print(answer2)
