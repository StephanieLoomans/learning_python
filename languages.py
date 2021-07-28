favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward':['ruby', 'go'],
	'phil':['python', 'haskell'],
}

for name, languages in favorite_languages.items():
	

#Show different text if only one language is picked

	if len(languages)==1:
		for language in languages:
			print(f"\n{name.title()}'s favorite language is {language.title()}.")


#show this if more than one language is picked
	elif len (languages)>1:
		print(f"\n{name.title()}'s favorite languages are:")
		for language in languages:
			print(f"\t{language.title()}")