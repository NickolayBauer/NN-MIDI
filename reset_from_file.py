from read_bin import load_on_file
import random

########################################################################
#
# Используемая функция:
# reset_from_file – восстаноление файла.
#
########################################################################
#
# Используемые переменные:
# path - путь к текстовым файлам;
# file - корневой файл;
# result - возвращаемый результат;
# empty_list - пустой массив;
# file_elem - элемент файла.
#
########################################################################

def reset_from_file(mass):
	path = "text_presets/"
	file = load_on_file(path+str(mass["classes"])+".txt")
	result = []
	empty_list = [0 for _, _ in enumerate(file)]
	for file_elem in file:
		if random.random() <= mass["probabilities"][mass["classes"]]:
			result.append(file_elem)
		else:
			result.append(empty_list)
	return result
