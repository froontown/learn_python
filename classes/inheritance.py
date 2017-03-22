# Notice we have a 'car.py' doc in the same folder. That's gonna be the parent, copied and pasted here:
# So! To create a class that has all the methods and attributes of the class 'Car', all you have to do is:

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

class ElectricCar(Car):
	"""Represents aspects of a car specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""Initialize the attributes of the parent class."""
		super().__init__(make, model, year)


# Defining attributes and methods for a child class
# Can add attributes and methods:

class ElectricCar(Car):
	"""Represents aspects of a car specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""Initialize the attributes of the parent class."""
		super().__init__(make, model, year)
		self.battery = 100

	def desc_battery(self):
		"""Print a statement describing how full the battery is."""
		print(f"This battery is at {self.battery} percent.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_description())
my_tesla.desc_battery()

# Overriding methods from the parent class
# Just define a method with the same name in the child class.
# If your classes are becoming intense, try to block out a new class
	# For example, if a the electric car's battery is getting complex, break it out into its own class then bring it into the ElectricCar class like so:

class Battery():
	"""A broken out battery class"""
	def __init__(self, battery_size=100):
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size} percent charge.")

class ElectricCar(Car):
	"""Represents aspects of a car specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""Initialize the attributes of the parent class."""
		super().__init__(make, model, year)
		self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_description())
my_tesla.battery.describe_battery()

