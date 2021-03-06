########################################################################
#
# Используемые функции:
# save_to_file – сохраняет данные в файл;
# load_on_file – загружает данные из файла.
#
########################################################################

########################################################################
#
# save_to_file – сохраняет данные в файл.
#
########################################################################
#
# Используемые переменные:
# f – файл;
# filename – имя файла;
# info – передаваемые данные;
# elem – элемент передаваемых данных.
#
########################################################################

def save_to_file(filename, info):
	f = open(filename+".txt", 'w')
	[f.write(str(elem)+"\n") for elem in info]

########################################################################
#
# load_on_file – сохраняет данные в файл.
#
########################################################################
#
# Используемые переменные:
# f – файл;
# filename – имя файла;
# elem – элемент файла.
#
########################################################################

def load_on_file(filename):
	f = open(filename, 'r').readlines()
	return [eval(elem) for elem in f]

