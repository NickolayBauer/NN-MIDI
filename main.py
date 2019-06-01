from neural_network import lets_go
from create_file_matrix_from_midi import create_bin_matrix
from reset_from_file import reset_from_file
from convert_to_matrix import matrix_to_note
from convert_to_midi import note_to_midi
from key import ord_note
import sys

########################################################################
#
# Используемые переменные:
# __main__ - определяет был ли модуль импортирован;
# sys.argv - системные аргументы, создавшиеся при запуске файла;
# c_arg - количество системных аргументов.
#
########################################################################
#
# Используемая функция:
# bedrock – осуществляет переключение между режимами выполнения.
#
########################################################################

########################################################################
#
# bedrock – осуществляет переключение между режимами выполнения.
#
########################################################################
#
# Используемые переменные:
# arg - содержит текст определяющий режим работы;
# name - имя сохраняемого файла;
# elem - элемент матрицы;
# row  - строка матрицы;
# r_notes - матричное представление файла;
# notes - вектор нот.
#
########################################################################

def bedrock(arg, name="result"):
	if arg == "work":
		print("Режим восстановления!\n\n")
		r_notes = [elem for row in [reset_from_file(elem) for elem in lets_go("work")] for elem in row]
		notes = (matrix_to_note(r_notes, 4))
		note_to_midi(name + ".mid", notes)
		print("Восстановлен файл '" + name+"'")

	elif arg == "train":
		print("Режим тренировки!\n\n")
		create_bin_matrix()
		lets_go("train")

	else:
		print("Необходимо указать корректную команду")


if __name__ == "__main__":
	c_arg = len(sys.argv)
	if c_arg > 2 and c_arg < 4:
		bedrock(sys.argv[1], sys.argv[2])
	elif c_arg == 2:
		bedrock(sys.argv[1])
	else:
		print("Неверное число команд")