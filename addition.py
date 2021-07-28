print("Give me two numbers, and I'll add them up.")
print("Enter 'q'to quit.") 

while True: 
	first_number = input("\n First number: ")
	if first_number == 'q':
		break
	second_number = input ("second_number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number)+int(second_number)
	except ValueError:
		print("You can only give numerical input!")
	else:
		print(answer)