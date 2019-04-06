import os
from read_bin import load_on_file
import numpy as np


def clear(file):
    row = []
    result = []
    #expression for x in iter1 for y in iter2
    for rows in file:
        for elem in rows:
            row.append([elem])
        result.append(row)
        row = []
    return result

def get_collect():
    #edu - на них нужно обучаться
    #root - его нужно разбивать на чанки и понимать
    path = "text_presets/"
    data_edu = []
    label_edu = []
    for i, elem in enumerate(os.listdir(path)):
        data_edu.append(clear(load_on_file(path+elem)))
        label_edu.append(i)
    return (np.array(data_edu[:2]), np.array(label_edu[:2]))

get_collect()
