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


#pause = 120 
#одна нота при 140bpm
def note_to_midi(save_file, notes):
	outfile = MidiFile()
	track = MidiTrack()
	outfile.tracks.append(track)

	track.append(Message('program_change', program=11))
	default_pause = 240
	pause = 0

	for i,default_elem in enumerate([key.ord_note(default_elem) for default_elem in notes]):
		if i != 0: pause = default_pause 
		if default_elem != -1:
			elem = default_elem
			track.append(Message('note_on', note=elem, velocity=100, time=pause))
			pause = default_pause
			track.append(Message('note_off', note=elem, velocity=100, time=pause))

		else:
			pause+=default_pause
			track.append(Message('note_on', note=elem, velocity=100, time=pause))
			pause = default_pause
			track.append(Message('note_off', note=elem, velocity=100, time=pause))


	outfile.save(save_file)



def midi_to_note(load_file, pause_time):
	list_notes = []
	mid = MidiFile(load_file)
	for track in mid.tracks:
		for msg in track:
			if msg.type == "note_on":
		 		if msg.time <= pause_time:
		 			for i in range(int(msg.time//pause_time)):
		 				list_notes.append("-")
		 	else:
		 		list_notes.append(key.chr_note(msg.note))

	return list_notes

print(midi_to_note("123.mid", 480))
note_to_midi("123.mid",["C5","-",'C5','-'])
print(midi_to_note("123.mid", 480))
