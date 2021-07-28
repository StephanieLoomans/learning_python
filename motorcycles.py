motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

motorcycles[0]= 'ducati'
print (motorcycles)

motorcycles.append('Harley Davidson')
print (motorcycles)

motorcycles.insert(4, 'mustang')
print (motorcycles)

del motorcycles[0]
print(motorcycles)

better_motorcycle = motorcycles.pop()
print(motorcycles)
print(better_motorcycle)

print(f"The last motorcycle I owned was a {better_motorcycle.title()}.")

motorcycles.remove('yamaha')
print(motorcycles)

too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too too expensive for me.")


