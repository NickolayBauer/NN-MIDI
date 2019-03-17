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

from convert_to_matrix import convert_to_matrix, matrix_to_note
from convert_to_midi import note_to_midi, midi_to_note
from read_bin import save_to_file, load_on_file
import os

def create_bin_matrix():
	path = "samples/"
	[save_to_file("text_presets/"+str(i),convert_to_matrix(midi_to_note(path+elem,0.27),4)) for i,elem in enumerate(os.listdir(path))]

def fun(one, two):
	print("cool!")

def nn():
	sample = load_on_file("example.txt")
	path = "text_presets/"
	for elem in os.listdir(path):
		fun(sample, load_on_file(path+elem))



nn()