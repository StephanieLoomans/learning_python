filename = 'python_learn.txt'

with open ('python_learn.txt') as file_object:
	lines = file_object.readlines()


	for line in lines:
		print(line.replace('Python', 'C'))