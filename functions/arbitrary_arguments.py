# An example using pizza toppings:
def make_pizza(*toppings):
	"""Print the list of toppings that have been requested."""
	print(toppings)

make_pizza('mushrooms')
make_pizza('mushrooms', 'sausage', 'pepperoni')

# Let's make the output more User readable:

def make_pizza(*toppings):
	"""Print a list of toppings"""
	print("We gon' make a pizza with these toppings: ")
	for topping in toppings:
		print(f"- {topping}")

make_pizza('hippos', 'gremlins', 'aphrodesiacs')


# Mixing positional and arbitrary arguments:
# Arbitrary arguments have to be last

def make_pizza(size, *toppings):
	print(f"Making a {size}-inch pizza with the following toppings: ")
	for topping in toppings:
		print(f"- {topping}")

make_pizza(12, 'raccoons', 'squirrels', 'kale')

# Using arbitrary keyword arguments
# This example is taking in User profiles with a for-sure first and last name, but other, unknown stuff:

def build_profile(first, last, **user_info):
	"""Build a hash containing everything we know about a User."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value # When calling the function, provide the key/value pairs needed:
	return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

