my_foods = [ 'pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]

my_foods.append('cannoli')
friends_food.append('ice cream')

print ('My favourite foods are:')
for food in my_foods [:]:
	print (food.title())

print('My friends foods are:')
for foodfriend in friends_food[:]:
	print (foodfriend.title())

