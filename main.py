from itertools import zip_longest
import math
import os
import test


#разбить по чанкам
def chunks(lst, count):
    return [list(elem) for elem in zip_longest(*[iter(lst)] * count, fillvalue = [0 for elem in range(len(lst[0]))]) ]

#прочитать все файлы
def go():
	path = "text_presets/"
	for elem in os.listdir(path):
		print(path+elem)

go()
