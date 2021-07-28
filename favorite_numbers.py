favorite_numbers = {
'dan':['9', '44', '55'],
'ahmed':['6', '12', '55'],  
'anna':['15', '4', '8'], 
'rik':['18', '77', '11'],
'irina':['21','24', '88'],
}

for name, numbers in favorite_numbers.items():
	print(f"\n{name.title()}'s favorite numbers are:")
	for number in numbers:
		print(f"\t{number}") 