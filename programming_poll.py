filename = 'reason_programming.txt'

with open (filename, 'a') as file_object:	
	while True:
		append_reason = input("Why do you like programming?")

		if append_reason== "":
			break

		else:
			file_object.write(f"Reason: {append_reason}\n")
			print ("Your reason has been added to the list!")
		