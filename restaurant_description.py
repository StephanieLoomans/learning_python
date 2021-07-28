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




served_restaurant = Restaurant('French', 'Paris', 45)
served_restaurant.increment_number_served(100)

print(f"{served_restaurant.restaurant_name} is a nice restaurant.")
print(f"This restaurant has a {served_restaurant.cuisine_type} cuisine.")
print(f"This restaurant is serving currently {served_restaurant.number_served}.")


class IceCreamStand (Restaurant):
	def __init__(self, cuisine_type, restaurant_name, number_served):
		super().__init__(cuisine_type, restaurant_name, number_served)
		self.flavors= "vanilla, strawberry, chocolate"

	def describe_flavors(self):
		print(f"This icecream stand called {self.restaurant_name} offers the following flavors of {self.cuisine_type}: {self.flavors}.")


my_icecreamstand = IceCreamStand('Italian icecream', 'Dulce', 5)
my_icecreamstand.describe_flavors()
