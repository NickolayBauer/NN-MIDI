#записать матрицу в файл
def save_to_file(filename, info):
	f = open(filename+".txt", 'w')
	[f.write(str(elem)+"\n") for elem in info]


#прочитать матрицу из файла
def load_on_file(filename):
	f = open(filename+'.txt', 'r').readlines()
	return [eval(elem) for elem in f]

#save_to_file('namefile', [[123],[1235],[12355]])  
#print(load_on_file('namefile'))