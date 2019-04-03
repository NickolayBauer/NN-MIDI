


def empty_array(ind, luft):
	empty_list = []
	mi = 5
	weight = 30
	for elem in range(2*12):
		if elem == ind:
			empty_list.append(30)
		elif abs(elem-ind) < 5 and abs(elem-ind)/2 == 1:
			empty_list.append(int(weight/abs(elem-ind)))
		else:
			empty_list.append(0)
	print(empty_list)



empty_array(4)
empty_array(9)
empty_array(14)
empty_array(10)
