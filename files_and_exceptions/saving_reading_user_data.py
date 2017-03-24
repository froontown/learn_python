# Storing User info that they enter:

# import json

# username = input("What is your username? ")

# file = 'username.json'

# with open(file, 'w') as f:
# 	json.dump(username, f)
# 	print(f"Your username hsa been stored, {username}!")

# With this stored, we can call it back in another program:

# import json

# filename = 'username.json'

# with open(filename) as f:
# 	username = json.load(f)
# 	print(f"Welcome back, {username}!")

# Let's merge the two into one file: if the username doesn't exist, it'll add it to username.json.

import json

# Load the Username if it has been stored previously
# If not, prompt the Username and store it

filename = 'username.json'

try:
	with open(filename) as f:
		username - json.load(f)
except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename, 'w') as f:
		json.dump(username, f)
		print(f"Your username has been stored as {username}.")
else:
	print(f"Welcome back, {froontown}!")

# Step by Step refactoring:

import json
# Move the program into a function:

def greet_user():
	"""Greet the User by name."""
	filename = 'username.json'

	try:
		with open(filename) as f:
			username - json.load(f)
	except FileNotFoundError:
		username = input("What is your name? ")
		with open(filename, 'w') as f:
			json.dump(username, f)
			print(f"Your username has been stored as {username}.")
	else:
		print(f"Welcome back, {froontown}!")

greet_user()

# Refactor the function so it isn't doing so many things:

import json

def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username

def greet_user():
	"""Greet the User by name."""
	username = get_stored_username()
	if username:
		print(f"Welcome back, {username}!")
	else:
		username = input("What is your name? ")
		filename = 'username.json'
		with open(filename, 'w') as f:
			json.dump(username, f)
			print(f"Your username has been stored as {username}.")		

greet_user()

# greet_user() is still prompting for a new name, so let's take that out and make it its own function, too

import json

def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""Prompt for a new username."""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username

def greet_user():
	"""Greet the User by name."""
	if username:
		print(f"Welcome back, {username}!")
	else:
		username = get_new_username()
		print("Your username has been stored as {username}.")	

greet_user()