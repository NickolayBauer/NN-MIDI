from neural_network import lets_go
from create_file_matrix_from_midi import create_bin_matrix
from reset_from_file import reset_from_file
from convert_to_matrix import matrix_to_note
from convert_to_midi import note_to_midi
import numpy as np
from key import ord_note
import sys

def bedrock(arg):
	if agr == "work":
		print("режим обучения!")
		#r_notes = [elem for row in [reset_from_file(elem) for elem in lets_go("work")] for elem in row]
		#notes = (matrix_to_note(r_notes, 4))
		#print([ord_note(elem) for elem in notes])
	
	elif arg == "train":
		print("режим тренировки!")
		#create_bin_matrix()
		#lets_go("train")
		#note_to_midi("beta.mid", notes)

	else:
		print("Нет такой команды!")

if __name__ == "__main__":
    for param in sys.argv:
        print(param)