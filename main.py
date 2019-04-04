from convert_to_matrix import convert_to_matrix, matrix_to_note, empty_array
from convert_to_midi import note_to_midi, midi_to_note
from read_bin import save_to_file, load_on_file
from itertools import zip_longest
import math
import os
import numpy as np
import test

####Создать файлы с матрицами	
def create_bin_matrix():
	save_to_file("example",convert_to_matrix(midi_to_note("example.mid"),4))
	path = "samples/"
	[save_to_file("text_presets/"+str(i),convert_to_matrix(midi_to_note(path+elem),4)) for i,elem in enumerate(os.listdir(path))]

#Что-то вроде свёртки
def mirror1(sample, preset):
	filter_kernel = [[1,0,1],
                     [0,5,0],
                     [1,0,1]]

	return test.test_max_pool(test.test_svert(sample, filter_kernel))

#разбить по чанкам
def chunks(lst, count):
    return [list(elem) for elem in zip_longest(*[iter(lst)] * count, fillvalue = [0 for elem in range(len(lst[0]))]) ]

def nn(sample, example, chunk):
	return [mirror1(np.array(exmpl), np.array(smpl)) for exmpl, smpl in zip(chunks(load_on_file(example),chunk), chunks(load_on_file(sample),chunk))]

def go():
	path = "text_presets/"
	for elem in os.listdir(path):
		print(elem+" ",nn("example.txt",  path+elem, 3))


go()
#create_bin_matrix()
