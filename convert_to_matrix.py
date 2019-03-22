import key

def empty_array(ind):
	return [30 if ind == i else 0 for i in range(2*12)]

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

