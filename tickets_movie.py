age = input("How old are you?")
age = int(age)

while True: 
	age = input(age)

	if age == 'complete':
		break
	if age >3 and age <= 12:
		print(f"Your ticket is $10.")
	if age >12:
		print(f"Your ticket is $15.")
	if age <= 3:
		print(f"Your ticket is for free.")