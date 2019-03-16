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

#Создадим список нот
#notes = "D5 B5 B5 A5 B5 G5 D5 D5 - D5 B5 B5 C6 E6 D6 - D6 E5 E5 C6 C6 B5 A5 G5 - D5 B5 B6 A5 B5 G5".split(" ")

#Запишем ноты в файл test.mid
#note_to_midi('test.mid', notes)

#Прочитаем ноты из файла
notes_str = midi_to_note('samples/1.mid', 0.3)
print(notes_str)
note_to_midi('clear1.mid',notes_str)

#Создадим матрицу из прочитанных нот
#matrix = convert_to_matrix(notes_str, 5)
#print("--Матрица--")
#[print(elem) for elem in matrix]
#print("\n")

#Преобразуем матрицу обратно в ноты
#print("--Преобразованные ноты из матрицы--\n",matrix_to_note(matrix, 5))