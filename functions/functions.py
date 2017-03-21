# Basic function syntax:

def greet():
	"""Display a simple greeting."""
	print("Hello!")

greet()

# Passing in an argument:

def greet_user(username):
	"""Display a simple greeting, taking a name as an argument"""
	print(f"Hello, {username.title()}!")

greet_user('froontown')