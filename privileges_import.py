
from user_import import User

class Privileges:
	def __init__(self, privileges = ['can add a post', 'can delete post', 'can ban user']):
		self.privileges = privileges

	def show_privileges(self):
		print(f"This admin user has the following rights: {self.privileges}.")


class Admin (User):
	def __init__ (self, first_name, last_name, user_name, date_of_birth, login_attempts):
		super().__init__(first_name, last_name, user_name, date_of_birth, login_attempts)
		self.privileges = Privileges()

	def describe_admin(self):
		print(f"This is the admin user: {first_name}, {last_name}, {user_name}")

