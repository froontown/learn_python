# Making a class:

class Dog():
	"""A simple dog class"""

	def __init__(self, name, age):
		"""the initialize method and attritbutes"""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog responding to the sit command."""
		print(f"{self.name.title()} is now sitting.")

	def roll_over(self):
		"""Simulate a dog responding to the roll over command."""
		print(f"{self.name.title()} rolled over! Just kidding he doesn't know that command.")

# Now let's make an instance of that class:

my_dog = Dog('piccolo', 12)
print(f"My dog's name is {my_dog.name.title()} and he is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

# Working with classes and instances\
# Let's set a default attribute "miles" that we can change:

# class Car():
# 	"""A car class. Duh."""

# 	def __init__(self, make, model, year):
# 		"""Initialize a car class"""
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odometer = 0

# 	def get_description(self):
# 		"""Return a formatted description."""
# 		full_name = f"{self.year} {self.make} {self.model}"
# 		return full_name.title()

# 	def read_odometer(self):
# 		"""Returns the car's mileage."""
# 		print(f"This car has {self.odometer} miles on it.")

# my_car = Car('honda', 'accord', 2001)
# print(my_car.get_description())
# # my_car.read_odometer()

# # Let's change the miles attribute directly:

# class Car():
# 	"""A car class. Duh."""

# 	def __init__(self, make, model, year):
# 		"""Initialize a car class"""
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odometer = 0

# 	def get_description(self):
# 		"""Return a formatted description."""
# 		full_name = f"{self.year} {self.make} {self.model}"
# 		return full_name.title()

# 	def read_odometer(self):
# 		"""Returns the car's mileage."""
# 		print(f"My car has {self.odometer} miles on it.")

# my_car.odometer = 250000 # Changing the self.odometer directly here
# my_car.read_odometer()

# Let's change the miles attribute through a method:

# class Car():
# 	"""A car class. Duh."""

# 	def __init__(self, make, model, year):
# 		"""Initialize a car class"""
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odometer = 0

# 	def get_description(self):
# 		"""Return a formatted description."""
# 		full_name = f"{self.year} {self.make} {self.model}"
# 		return full_name.title()

# 	def read_odometer(self):
# 		"""Returns the car's mileage."""
# 		print(f"My car has {self.odometer} miles on it.")

# 	def update_odometer(self, miles):
# 		"""Set the odometer to the number of miles given."""
# 		self.odometer = miles

# my_car = Car('honda', 'accord', 2001)
# print(my_car.get_description())
# my_car.update_odometer(500)
# my_car.read_odometer()

# Let's change the miles by incrementing them through a method:

class Car():
	"""A car class. Duh."""

	def __init__(self, make, model, year):
		"""Initialize a car class"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer = 0

	def get_description(self):
		"""Return a formatted description."""
		full_name = f"{self.year} {self.make} {self.model}"
		return full_name.title()

	def read_odometer(self):
		"""Returns the car's mileage."""
		print(f"My car has {self.odometer} miles on it.")

	def update_odometer(self, miles):
		"""Set the odometer to the number of miles given."""
		self.odometer = miles

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer."""
		self.odometer += miles

my_car = Car('honda', 'accord', 2001)
print(my_car.get_description())
my_car.update_odometer(500)
my_car.read_odometer()
my_car.increment_odometer(1)
my_car.read_odometer()