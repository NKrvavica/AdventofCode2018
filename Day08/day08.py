# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 22:45:26 2018

@author: Nino
"""

import numpy as np

fname = 'input.txt'

data = np.loadtxt(fname, dtype='int32')


def add_metadata(data, n, counter):
    children, meta = data[n:n+2]
    n += 2
    if children > 0:
        for c in range(children):
            n, counter = add_metadata(data, n, counter)
    metadata = data[n:n+meta]
    counter += metadata.sum()
    n += len(metadata)
    return n, counter


counter, n = 0, 0
n, counter = add_metadata(data, n, counter)
print(counter)


def find_root_value(data, n, counter):

    children, meta = data[n:n+2]
    n += 2

    # node with children
    if children > 0:

        # get children node values
        child_node_values = {}
        for c in range(children):
            n, node_value = find_root_value(data, n, counter)
            child_node_values[c+1] = node_value

        # get parent node value
        metadata = data[n:n+meta]
        node_value = 0
        for data in metadata:
            if data in child_node_values:
                node_value += child_node_values[data]

    else:  # node without child
        metadata = data[n:n+meta]
        node_value = metadata.sum()

    n += len(metadata)
    return n, node_value


node_value, n = 0, 0
n, node_value = find_root_value(data, n, counter)
print(node_value)
