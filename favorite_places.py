favorite_places = {
	'omnia': ['scotland', 'sushi restaurant', 'cairo'],
	'irina': ['tribes', 'delft', 'moscow'],
	'alex': ['nice', 'gym', 'mediterranean sea'],
}


for name, places in favorite_places.items():
	print(f"\n{name.title()}'s favorite places are:")
	for place in places:
		print(f"\t{place.title()}") 