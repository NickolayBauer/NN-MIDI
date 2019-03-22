from mido import Message, MidiFile, MidiTrack
import sys
import key

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

