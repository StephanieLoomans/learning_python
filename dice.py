class Die:
	def __init__(self,sides):
		self.sides=6

	def roll_die(self):
		values = [1,2,3,4,5,6]
		roll_die= choice(values)