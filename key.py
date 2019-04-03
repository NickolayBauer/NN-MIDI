from re import findall

note_list = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

def ord_note(note):
	if note == "-": return -1
	octava = int(findall(r'[0-9]',note)[0])
	ind = note_list.index(''.join(findall(r'\D',note)))
	return ind + octava*12

def chr_note(ind):
	return note_list[ind%12]+str(ind//12)