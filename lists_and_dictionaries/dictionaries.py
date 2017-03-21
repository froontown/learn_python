# Look like hashes to me:

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_color = alien_0['color']
print(alien_color)
earned_points = alien_0['points']
print(earned_points)

# Adding Key/Value pairs:
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Modifying a value:
alien_0['color'] = 'orange'
print(alien_0)

# Gonna move this alien around by changing `x_position` based on the key/value pair of `speed`:
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

print("Original x-position: " + str(alien_0['x_position']))
# Original x-position: 0

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))
# New x-position: 2

# Deleting a key/value pair:

alien_0 = {'color': 'green', 'points': 5}

del alien_0['points']
print(alien_0)

# Loopin!
user_0 = {
	'username': 'froontown',
	'first_name': 'froon',
	'last_name': 'town',
	}

for key, value in user_0.items(): # `key, value` are the variables you're defining. They could be `odd, zook` or `k, v` or whatever
	print("\nKey: " + key)
	print("Value: " + value)

# Print just keys:
for key in user_0.keys():
	print(key)
# or
for key in user_0:
	print(key)

friends = ['ben', 'tori', 'jon', 'katherine']
favorite_languages = {
	'ben': 'python',
	'evan': 'C#',
	'kalen': 'JavaScript',
	'tori': 'ruby',
	'jon': 'JavaScript',
	}

for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print(" Hi " + name.title() + ", your fave language is " + favorite_languages[name].title()+ "!")

# If for some reason you wanna return Keys in order:
# We'll wrap `favorite_languages.keys()` in `sorted()` to sort things before looping through it:
for name in sorted(favorite_languages.keys()):
	print(name.title())

# Looping through Values:
for value in favorite_languages.values():
	print(value.title())
print('======')

# To avoid repetition, use `set()`
for value in set(favorite_languages.values()):
	print(value.title())

# Nesting (array in array, etc.)
alien_0 = {
	'color': 'green',
	'points': 5,
	}

alien_1 = {
	'color': 'yellow',
	'points': 10,
	}

alien_2 = {
	'color': 'red',
	'points': 15,
	}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

# Let's make 30 green aliens using `range()`
aliens = []

for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# Looping through a slice to make some green aliens yellow and a little faster:

for alien in aliens[0:11]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'

print(aliens[:16])

# Putting an array/list into a hash/dictionary:
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'sausage'],
	}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
	print(f"\t{topping}")

# Hashes/Dictionaries within hashes/dictionaries:
users = {
	'froontown': {
		'first_name': 'froon',
		'last_name': 'town',
		'location': 'boston',
		},
	'honeybear': {
		'first_name': 'honey',
		'last_name': 'bear',
		'location': 'imaginationland',
		},
	}

for username, user_data in users.items():
	print(f"\nUsername: {username}")
	full_name = user_data['first_name'] + " " + user_data['last_name']
	location = user_data['location']

	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")