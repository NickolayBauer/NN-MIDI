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

# def filter_note(notes):
# 	clear_list = [notes[0]]
# 	for i,elem in enumerate(notes):
# 		try:
# 			if notes[i-1] == "-":
# 				if elem == "-":
# 					clear_list.append(elem)
# 			else:
# 				clear_list.append(elem)
# 		except:
# 			print(elem)
# 			clear_list.append(elem)
# 	return clear_list


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
			

		else:
			pause+=default_pause
		track.append(Message('note_on', note=elem, velocity=100, time=pause))
		pause = default_pause
		track.append(Message('note_off', note=elem, velocity=100, time=pause))

	outfile.save(save_file)



def midi_to_note(load_file):
	mid = MidiFile(load_file)
	time_list = []
	list_notes = []

	for track in mid.tracks:
		for msg in track:
			if msg.type == "note_on" or msg.type == "note_off":
				time_list.append(msg.time)

	pause_time =  max(set(time_list), key=time_list.count)

	for track in mid.tracks:
		for msg in track:
			if msg.type == "note_on" and msg.time > 0:
				for i in range(int(msg.time//pause_time)):
					list_notes.append("-")
			elif msg.type == "note_off": 
				list_notes.append(key.chr_note(msg.note))

	return list_notes

