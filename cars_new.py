def build_car(brand, type, **car_info):
	car_info['brand']= brand
	car_info['type']= type 
	return car_info

car_profile = build_car('ford', 'fiesta', hp= '95', accessoiry= 'comfortpack')

print(car_profile)