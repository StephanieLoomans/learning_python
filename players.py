players = [ 'charles', 'martina', 'michael', 'florence', 'eli', 'harry']

print ("Here are the players in my team:")
for player in players[:3]:
	print(player.title())


print ("The first three items in the list are:")
for player in players [:3]:
	print(player.title())


print ("The three items in the middle of the list are:")
for player in players [1:4]:
	print(player.title())

print ("The last three items of the list are:")
for player in players [-3:]:
	print(player.title())