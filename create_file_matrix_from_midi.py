from convert_to_matrix import convert_to_matrix as ctx
from convert_to_midi import note_to_midi, midi_to_note
from read_bin import save_to_file, load_on_file
import os

def create_bin_matrix():
	exmpl = ctx(midi_to_note("example.mid"), 4)
	save_to_file("example", exmpl)
	path = "samples/"
	[save_to_file("text_presets/"+str(i), ctx(midi_to_note(path+elem),4)) for i, elem in enumerate(os.listdir(path))]
	c_f = len(os.listdir(path))
	print("Done! Преобразовано ", c_f," файлов + корневой")

