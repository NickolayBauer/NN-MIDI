from read_bin import load_on_file
import random

def reset_from_file(mass):
	path = "text_presets/"
	file = load_on_file(path+str(mass["classes"])+".txt")
	result = []
	empty_list = [0 for _ , _ in enumerate(file)]
	for file_elem in file:
		if random.random() <= mass["probabilities"]:
			result.append(file_elem)
		else:
			result.append(empty_list)
	return result