import sys
import key

from mido import Message, MidiFile, MidiTrack

# Используемые функции:
# note_to_midi() - преобразование массива нот в аудиофайл;
# midi_to_note() - преобразование аудиофайла в массив нот.

# Используемые переменные:
# outfile - объект класса MidiFil;
# track - объект класса MidiTrack;
# delta - пауза между нотами;
# default_delta - сохранённая delta;
# pause_coef - коэффициент паузы;
# ticks_per_expr - количество ударов в минуту;
# elem - элемент списка;
# notes - массив нот;
# note - нота;
# pitch - копия основного сигнала;
# j - индекс;
# save_file - имя сохраняемого файла;
# load_file - имя загружамоего файла;
# list_notes - массив нот;
# pause_time - время паузы;
# mid - объект класса MidiFile;
# msg - элемент mid.

def note_to_midi(save_file, notes):
	outfile = MidiFile()

	track = MidiTrack()
	outfile.tracks.append(track)

	track.append(Message('program_change', program=12))

	delta = 250
	default_delta = delta
	pause = False

	pause_coef = 1.5
	ticks_per_expr = 90
	for elem in [key.ord_note(elem) for elem in notes]:
		if elem != -1:
			note = elem
			track.append(Message('note_on', note=note, velocity=100, time = int(delta*pause_coef) if pause else delta))
			pause = False
			for j in range(delta // ticks_per_expr):
				pitch =  ticks_per_expr // delta
				track.append(Message('pitchwheel', pitch=pitch, time=ticks_per_expr))
			track.append(Message('note_off', note=note, velocity=100, time=0))
		else:
			pause = True

	outfile.save(save_file)



def midi_to_note(load_file, pause_time):
	list_notes = []
	mid = MidiFile(load_file)
	for msg in mid:
		print(msg)
		if msg.type == "note_on":
	 		if msg.time > 0.3:
	 			list_notes.append("-")
	 		list_notes.append(key.chr_note(msg.note))

	return list_notes