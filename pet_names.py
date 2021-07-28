def  read_text (filename):

	try:
		with open (filename, encoding= 'utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		pass
	else:
		print(contents)

filenames = [ 'cats.txt', 'dogs.txt', 'horses.txt']
for filename in filenames:
	read_text(filename)