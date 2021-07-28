class Restaurant:
	def __init__(self, cuisine_type, restaurant_name, number_served):
			self.cuisine_type= cuisine_type
			self.restaurant_name=restaurant_name
			self.number_served=number_served

	def name(self):
		print(f"{self.restaurant_name} is a nice restaurant.")
	def cuisine(self):
		print(f"This restaurant has a {self.cuisine_type} cuisine.")
	def set_number_served(self):
		print(f"{self.number_served} people have been served.")
	def increment_number_served(self, guests):
		self.number_served += guests