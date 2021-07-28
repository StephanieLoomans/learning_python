def describe_city (city, country='germany'):
	print(f"{city.title()} is in {country.title()}.")

describe_city(city='berlin')
describe_city(city='Munich')
describe_city(city='Amsterdam', country='the netherlands')