# Отчет по производственной практике 01
# по теме: Создание API для подготовки выборки, использующейся в нейронной сети.
# Разработал: Лосев Николай Дмитриевич ТМП-82
# Используемый язык программирования: Python
#
# Задание:
# Реализовать API, позволяющее преобразовывать midi – файлы в нотную текстовую запись и подготовить данные, которые сможет использовать нейронная сеть. 
#
# Используемые функции:
# convert_to_matrix() - преобразование нотной записи в матрицу;
# matrix_to_note() - преобразование матрицы в нотную запись;
# note_to_midi() - преобразование нотной записи в midi - файл;
# midi_to_note() - преобразование midi - файла в нотную запись.

#Используемые переменные:
# notes - список нот;
# notes_str - текстовая запись нот;
# matrix - матрица созданная из нотной записи.

from convert_to_matrix import convert_to_matrix, matrix_to_note, empty_array
from convert_to_midi import note_to_midi, midi_to_note
from read_bin import save_to_file, load_on_file
from itertools import zip_longest
import os

def create_bin_matrix():
	path = "samples/"
	[save_to_file("text_presets/"+str(i),convert_to_matrix(midi_to_note(path+elem),4)) for i,elem in enumerate(os.listdir(path))]

def mirror(sample, preset):
		weight = 0
		for i, _ in enumerate(preset):
			for j, _ in enumerate(preset[0]):
				weight += sample[i][j] * preset[i][j]
		return weight
		
def chunks(lst, count):
    return [list(elem) for elem in zip_longest(*[iter(lst)] * count, fillvalue = [0 for elem in range(len(lst[0]))]) ]


def nn(sample, example, chunk):
	return [mirror(exmpl, smpl) for exmpl, smpl in zip(chunks(load_on_file(example),chunk), chunks(load_on_file(sample),chunk))]


#for i in range(5):
#	print(nn("example.txt", "text_presets/"+str(i)+".txt", 2))


#save_to_file("example", convert_to_matrix(midi_to_note("example.mid",480),4))

save_to_file("example",convert_to_matrix(midi_to_note("example.mid"),4))