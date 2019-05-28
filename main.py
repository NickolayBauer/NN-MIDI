from neural_network import lets_go
from create_file_matrix_from_midi import create_bin_matrix
from reset_from_file import reset_from_file
from convert_to_matrix import matrix_to_note
from convert_to_midi import note_to_midi
from key import ord_note
import sys


def bedrock(arg, name="result"):
	if arg == "work":
		print("режим обучения!")
		r_notes = [elem for row in [reset_from_file(elem) for elem in lets_go("work")] for elem in row]
		notes = (matrix_to_note(r_notes, 4))
		note_to_midi(name + ".mid", notes)

	elif arg == "train":
		print("режим тренировки!")
		create_bin_matrix()
		lets_go("train")

	else:
		print("Необходимо указать корректную команду")


if __name__ == "__main__":
	if len(sys.argv) > 2 and len(sys.argv) < 4:
		bedrock(sys.argv[1], sys.argv[2])
	elif len(sys.argv) == 2:
		bedrock(sys.argv[1])
	else:
		print("Неверное число команд")