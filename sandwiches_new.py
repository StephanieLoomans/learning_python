def make_sandwich(*spreads):
	print("\nMaking a sandwich with the following spreads:")
	for spread in spreads:
		print(f"-{spread}")

make_sandwich('cheese', 'butter')
make_sandwich('pastrami')
make_sandwich('peanut butter', 'bacon', 'pineapple')