current_users = [ 'harry', 'peter', 'Joanna', 'Diego', 'ANN']
current_users_2 = []

for current_user in current_users:
	current_users_2.append(current_user.lower())

new_users = ['Harry', 'donald', 'Kim Jung Un', 'Ji Xiao']
new_users_2 = []

for new_user in new_users:
	new_users_2.append(new_user.lower())


for new_user_2 in new_users_2:
	if new_user_2 in current_users_2:
		print (f"Hi {new_user_2.title()}, you need to create a new username.")

	else:
		print (f"Hi {new_user_2.title()} , This user name is available")

