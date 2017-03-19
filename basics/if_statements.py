# Basic loop where if the item in the array 'cars' == 'honda', make it all caps
cars = ['accord', 'civic', 'honda', 'camry']

for car in cars:
	if car == 'honda':
		print(car.upper())
	else:
		print(car.title())

# Can do things to set the case or something in case it doesn't amtter:
a = 'AAA'
a.lower() == 'aaa'
# returns True

# Other checks:
# ==, !=, <=, >=

# `and` is the same as `&&`
age_0 = 22
age_1 = 18
age_0 >= 22 and age_1 <= 21 # Returns true

# `or` is the same as `||`
age_0 >=21 or age_1 >= 21 # Returns true

# `in` and `not in` is the same as `.include?`
'accord' in cars # returns True

'4runner' not in cars # returns True
suv = '4runner'

if suv not in cars:
	print(suv.title() + ' is not in cars') # 4Runner is not in cars

