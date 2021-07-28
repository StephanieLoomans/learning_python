def make_shirt(size = "L", text = "I love Python"):
	print(f"The customer ordered a t-shirt with size {size} and the following message should be printed on it: '{text.title()}'.")

make_shirt()
make_shirt(size = 'M', text = "I am a mad man")