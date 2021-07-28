class User:
	def __init__(self, first_name, last_name, user_name, date_of_birth, login_attempts):
		self.first_name = first_name
		self.last_name = last_name
		self.user_name = user_name
		self.date_of_birth = date_of_birth
		self.login_attempts = login_attempts

	def login(self):
		print(f"{self.user_name} has logged in.")

	def reset(self):
		print(f"{self.first_name} {self.last_name} has resetted his/her password.")

	def logout(self):
		print(f"{self.user_name} has logged out.")

	def describe_user(self):
		print(f"{self.user_name} is in real life {self.first_name} {self.last_name} and is born on {self.date_of_birth}.")

	def greet_user(self):
		print(f"Welcome {self.first_name} {self.last_name}!")
	def first_attempt(self):
		print(f"{self.user_name} has tried to login {self.login_attempts} time(s).")

	def increment_login_attempts(self, attempts):
		self.login_attempts += attempts
	def reset_login_attempts(self):
		self.login_attempts = 0



