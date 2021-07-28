filename = 'mobydick.txt'

try:
	with open (filename, encoding= 'utf-8') as f:
		contents = f.read()
except FileNotFoundError:
	print(f"sorry, the file {filename} does not exist.")
else:
	words = contents.lower().count('the ')
	print(f"The file {filename} has about {words} words saying 'the'.")


