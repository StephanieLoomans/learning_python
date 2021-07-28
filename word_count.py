def count_words(filename):

	try:
		with open(filename, encoding= 'utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		pass
	else:
		# Count the approximate number of words in the file.
		words= contents.split()
		num_words = len(words)
		print(f"The file {filename} has about {num_words} words.")

filenames = ['siddhartha.txt', 'alice.txt', 'mobydick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)