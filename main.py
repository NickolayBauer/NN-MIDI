import math
import os
import test

#прочитать все файлы
def go():
	path = "text_presets/"
	for elem in os.listdir(path):
		print(path+elem)

go()
