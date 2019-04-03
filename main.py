from convert_to_matrix import convert_to_matrix, matrix_to_note, empty_array
from convert_to_midi import note_to_midi, midi_to_note
from read_bin import save_to_file, load_on_file
from itertools import zip_longest
import test
import math
import os
import numpy as np

####Создать файлы с матрицами	
def create_bin_matrix():
	save_to_file("example",convert_to_matrix(midi_to_note("example.mid"),4))
	path = "samples/"
	[save_to_file("text_presets/"+str(i),convert_to_matrix(midi_to_note(path+elem),4)) for i,elem in enumerate(os.listdir(path))]

#Что-то вроде свёртки
def mirror1(sample, preset):
		weight = 0
		for i, _ in enumerate(preset):
			for j, _ in enumerate(preset[0]):
				weight += sample[i][j] * preset[i][j]
		return weight

#разбить по чанкам
def chunks(lst, count):
    return [list(elem) for elem in zip_longest(*[iter(lst)] * count, fillvalue = [0 for elem in range(len(lst[0]))]) ]

def nn(sample, example, chunk):
	return [mirror1(np.array(exmpl), np.array(smpl)) for exmpl, smpl in zip(chunks(load_on_file(example),chunk), chunks(load_on_file(sample),chunk))]

def go():
	for i in range(5):
		print(str(i)+".txt\n")
		print([elem for elem in nn("example.txt", "text_presets/"+str(i)+".txt", 3)])


go()
#create_bin_matrix()