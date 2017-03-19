# Basic loop where if the item in the array 'cars' == 'honda', make it all caps
cars = ['accord', 'civic', 'honda', 'camry']

for car in cars:
	if car == 'honda':
		print(car.upper())
	else:
		print(car.title())
