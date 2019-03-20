list_1 = [i for i in range(10)]
list_2 = [j for j in range(5,10)]
print(list_1, list_2)

for elem_1, elem_2 in zip(list_1, list_2):
	print(elem_1, '  ', elem_2)


names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']
for name, color in zip(names, colors):
    print (name, '-->', color)