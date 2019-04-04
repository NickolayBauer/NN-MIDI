import key

def empty_array(ind):
	half_koef = 0.7
	full_koef = 0.9
	empty_list = []
	mi = 5
	weight = 30
	if "#" in key.chr_note(ind): half_tone = True
	else: half_tone = False


	for elem in range(2*12):
		if elem == ind:
			empty_list.append(30)
		elif abs(elem-ind) < 5:
			if (half_tone == True) and ("#" in key.chr_note(elem)):
				empty_list.append(int(weight/abs(elem-ind)*half_koef))
			elif half_tone == False and "#" not in key.chr_note(elem):
				empty_list.append(int(weight/abs(elem-ind)*full_koef))
			else:
				empty_list.append(0)
		else:
			empty_list.append(0)
	return empty_list

def convert_to_matrix(notes_array, luft):
	return [empty_array(key.ord_note(elem)-luft*12) for elem in notes_array]

def matrix_to_note(mass, luft):
	return_list = []
	for elem in mass:
		try:
			return_list.append(key.chr_note(elem.index(1)+luft*12))
		except:
			return_list.append("-")

	return return_list

