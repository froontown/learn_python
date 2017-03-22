# Make a restaurant class with number of folk served: [X]
# Add a number of customers served to the restaurant: [X]
# Add a number of customers via a method: 			  [X]
# Use an increment method to the number served:		  [X]

# Make a User class with a first and last name:       [ ]
# Make a method that describes the User:              [ ]
# Make a method that greetrs the User:                [ ]
# Count how many times a User logs in:				  [ ]
# Create a way to reset the login counter:            [ ]


class Restaurant():
	"""A restaurant class"""

	def __init__(self, name, cuisine):
		"""The initialize method for the restaurant class."""
		self.name = name
		self.cuisine = cuisine
		self.num_served = 0

	def describe(self):
		"""A description of the restaurant and cuisine type."""
		print(f"{self.name.title()} is a restaurant with a {self.cuisine.title()} cuisine.")

	def print_num_served(self):
		"""Outputs the number of customers served."""
		print(f"{self.name.title()} has served {self.num_served} customers.")

	def update_num_served(self, num):
		"""Set the num_served via a method like so."""
		if num >= self.num_served:
			self.num_served = num
		else:
			print("That don't work.")

	def increment_num_served(self, num):
		"""Increment the number served."""
		self.num_served += num

dahmee = Restaurant('dahmee', 'thai')
dahmee.describe()
dahmee.num_served = 140
dahmee.update_num_served(141)
dahmee.print_num_served()
dahmee.increment_num_served(90000)
dahmee.print_num_served()

class User():
	"""A User class"""

	def __init__(self, first, last):
		self.first = first
		self.last = last
		self.logins = 0

	def describe(self):
		"""Prints a summary of the User's name"""
		print(f"The User's name is {self.first.title()} {self.last.title()}.")

	def greet(self):
		"""Greets the User."""
		print(f"Hello, {self.first.title()} {self.last.title()}!!!")

	def display_logins(self):
		print(f"{self.first.title()} {self.last.title()} has logged in {self.logins} times.")

	def increment_login(self):
		"""Increments number of times logged in when called."""
		self.logins += 1

	def reset_login(self):
		"""Resets login counter."""
		self.logins = 0

me = User('froon', 'town')
me.describe()
me.greet()
me.increment_login()
me.increment_login()
me.increment_login()
me.display_logins()
me.reset_login()
me.display_logins()