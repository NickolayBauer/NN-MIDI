from key import chr_note

def empty_array(ind):
	empty_list = []
	mi = 5
	weight = 30
	if "#" in chr_note(ind): half_tone = True
	else: half_tone = False


	for elem in range(2*12):
		if elem == ind:
			empty_list.append(30)
		elif abs(elem-ind) < 5:
			if (half_tone == True) and ("#" in chr_note(elem)):
				empty_list.append(int(weight/abs(elem-ind)*0.2))
			elif half_tone == False and "#" not in chr_note(elem):
				empty_list.append(int(weight/abs(elem-ind)))
			else:
				empty_list.append(0)
		else:
			empty_list.append(0)
	return empty_list
 


empty_array(1)
empty_array(9)
empty_array(14)
empty_array(10)
