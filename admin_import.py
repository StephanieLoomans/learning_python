class Admin (User):
	def __init__ (self, first_name, last_name, user_name, date_of_birth, login_attempts):
		super().__init__(first_name, last_name, user_name, date_of_birth, login_attempts)
		self.privileges = Privileges()

	def describe_admin(self):
		print(f"This is the admin user: {first_name}, {last_name}, {user_name}")