from convert_to_matrix import convert_to_matrix, matrix_to_note, empty_array
from convert_to_midi import note_to_midi, midi_to_note
from read_bin import save_to_file, load_on_file
from itertools import zip_longest
import test
import math
import os
import numpy as np

def sigmoid(x):
	return 1/(1+math.exp(-x))

def gtang(x):
	return 2/(1+math.exp(-2*x))-1

def reverse_square(x):
	pass
	
def create_bin_matrix():
	path = "samples/"
	[save_to_file("text_presets/"+str(i),convert_to_matrix(midi_to_note(path+elem),4)) for i,elem in enumerate(os.listdir(path))]

def mirror1(sample, preset):
		weight = 0
		for i, _ in enumerate(preset):
			for j, _ in enumerate(preset[0]):
				weight += sample[i][j] * preset[i][j]
		return weight

		
def chunks(lst, count):
    return [list(elem) for elem in zip_longest(*[iter(lst)] * count, fillvalue = [0 for elem in range(len(lst[0]))]) ]

def nn(sample, example, chunk):
	other={
	'convolution':False,
	'stride':1,
	'center_w_l':(0,0)
	}
	#test.convolution_feed_x_l(np.array(exmpl), np.array(smpl), other)
	return [test.convolution_feed_x_l(np.array(exmpl), np.array(smpl), other) for exmpl, smpl in zip(chunks(load_on_file(example),chunk), chunks(load_on_file(sample),chunk))]

def go():
	for i in range(5):
		print(str(i)+".txt\n")
		[print(elem) for elem in nn("example.txt", "text_presets/"+str(i)+".txt", 2)]
	#save_to_file("example",convert_to_matrix(midi_to_note("example.mid"),4))

go()
