import key

########################################################################
#
# Используемые функции:
# empty_array – создаёт вектор;
# convert_to_matrix - преобразует данные в матрицу;
# matrix_to_note - преобразует матрицу в нотный вектор.
#
########################################################################

########################################################################
#
# empty_array – создаёт вектор.
#
########################################################################
#
# Используемые переменные:
# half_koef - коэфициент добавления веса в вектор при полутоне;
# full_koef - коэфициент добавления веса в вектор при чистой ноте;
# empty_list - вектор весов;
# mi - удалённость текущего элемента от ноты;
# how_octav - сколько октав задейстововано;
# weight - вес;
# elem - элемент вектора;
# ind - индекс ноты.
#
########################################################################

def empty_array(ind):
	half_koef = 0.8
	full_koef = 0.85
	empty_list = []
	mi = 3
	how_octav = 2
	weight = 255
	
	if "#" in key.chr_note(ind): half_tone = True
	else: half_tone = False

	for elem in range(how_octav*12):
		if elem == ind:
			empty_list.append(weight)
		elif abs(elem-ind) <= mi:
			if (half_tone == True) and ("#" in key.chr_note(elem)):
				empty_list.append(int(weight/abs(elem-ind)*half_koef))
			elif half_tone == False and "#" not in key.chr_note(elem):
				empty_list.append(int(weight/abs(elem-ind)*full_koef))
			else:
				empty_list.append(0)
		else:
			empty_list.append(0)
	return empty_list

########################################################################
#
# convert_to_matrix - преобразует данные в матрицу.
#
########################################################################
#
# Используемые переменные:
# result - результат преобразования;
# notes_array - список нот;
# elem - элемент списка нот;
# luft - смещение по октавам.
# 
########################################################################

def convert_to_matrix(notes_array, luft):
	result = [empty_array(key.ord_note(elem)-luft*12) for elem in notes_array]
	return result

########################################################################
#
# matrix_to_note - преобразует матрицу в нотный вектор.
#
########################################################################
#
# Используемые переменные:
# return_list - список для нот;
# mass - матрица;
# lust - смещение по откавам;
# elem - элемент списка нот;
# luft - смещение по октавам;
# max - максимальный вес в векторе.
#
########################################################################

def matrix_to_note(mass, luft):
	return_list = []
	for elem in mass:
		m = max(elem)
		if m == 0:
			return_list.append("-")
		else:
			return_list.append(key.chr_note(elem.index(m)+luft*12))
	return return_list
