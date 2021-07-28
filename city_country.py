def city_country (city, country):
	"""Print value pairs of cities and countries"""
	cityandcountry= f"{city.title()}, {country.title()}"
	return cityandcountry

message = city_country('amsterdam', 'netherlands')
print(message)