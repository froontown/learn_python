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

# if else && if-elif-else chains:
age = 17

if age >= 18:
	print("You can vote, yo!")
else:
	print("Can't vote yet, yo!")

age_2 = 12

if age < 4:
	print("Your ticket is free!")
elif age < 18:
	print ("Your ticket is $5!")
else:
	print("Your ticket is $10!")

# Practice:
alien_color = 'green'

if alien_color == 'green':
	print('Player earned 5 points!')
elif alien_color == 'red':
	print('Player earned 10 points!')
else:
	print('Player earned 15 points!')

# Check for special items:
# This is a contrived example of a pizza shop that doesn't have a certain topping during a `for` loop:

toppings = ['mushrooms', 'pepperoni', 'green peppers', 'anchovies']

for topping in toppings:
	if topping == 'anchovies':
		print(f"Sorry, we don't got no {topping}.")
	else:
		print(f'Added {topping}!')
print("\nPizza's all done!")

# Check that a list isn't empty:

empty = []

if empty:
	print("This won't output")
else:
	print("List is empty")

# Checking through multiple lists:
cars = ['mustang', 'viper', 'kitt', 'delorean']
others = ['toaster', 'hippo', 'rhino', 'kitt']

for other in others:
	if other in cars:
		print(f'{other} is in the list')
	else:
		print(f'{other} is not in the list')

print("\n List's all done!")