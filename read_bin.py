def save_to_file(filename, info):
	f = open(filename+".txt", 'w')
	[f.write(str(elem)+"\n") for elem in info]

def load_on_file(filename):
	f = open(filename, 'r').readlines()
	return [eval(elem) for elem in f]

