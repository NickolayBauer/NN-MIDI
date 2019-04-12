from convert_to_matrix import convert_to_matrix, matrix_to_note, empty_array
from convert_to_midi import note_to_midi, midi_to_note
from read_bin import save_to_file, load_on_file
import os

def create_bin_matrix():
    save_to_file("example",convert_to_matrix(midi_to_note("example.mid"),4))
    path = "samples/"
    [save_to_file("text_presets/"+str(i),convert_to_matrix(midi_to_note(path+elem),4)) for i,elem in enumerate(os.listdir(path))]
    print("Done! Преобразовано ",len(os.listdir(path))," файлов + корневой")

if __name__ == '__main__':
    create_bin_matrix()
