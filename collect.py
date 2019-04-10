import os
from read_bin import load_on_file
import numpy as np
from itertools import zip_longest

#разбить по чанкам
def chunks(lst, count):
    return [list(elem) for elem in zip_longest(*[iter(lst)] * count, fillvalue = [0 for elem in range(len(lst[0]))]) ]


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
    data_work = []
    for i, elem in enumerate(os.listdir(path)):
        data_edu.append(clear(load_on_file(path+elem)))
        label_edu.append(i)

    for elem in chunks(load_on_file("example.txt"),24):
        data_work.append(clear(elem))
    return np.array(data_edu), np.array(label_edu),np.array(data_work)
