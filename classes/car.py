class Car():
	"""A simple representation of a car."""

	def __init__(self, make, model, year):
		"""Initialize attributes to a car"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Returns a formatted description."""
		full_name = f"{self.year} {self.make} {self.model}"
		return full_name.title()

	def read_odometer(self):
		"""Returns the odometer reading"""
		print(f"The odometer reads {self.odometer_reading} miles.")

	def update_odometer(self, miles):
		"""Manually update the odometer through a method."""
		"""Doesn't allow rolling back miles"""
		if miles >= self.odometer_reading:
			self.odometer_reading = miles
		else:
			print("You can't roll back miles, sonn!!!")

	def increment_odometer(self, miles):
		"""Increment the odometer via a method."""
		self_odometer_reading += miles

class Battery():
	"""A basic battery class"""

	def __init__(self, battery_size=100):
		"""Initialize the battery class"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print out battery supply."""
		print(f"The battery charge is at {self.battery_size} percent.")

	def get_range(self):
		"""Print about the range of the battery."""
		if self.battery_size == 75:
			range = 300
		elif self.battery_size == 100:
			range = 100

		message = f"This car can go approximately {range} miles."
		print(message)

class ElectricCar(Car):
	"""Takes stuff from the car class and creates its own differences as an Electric Car."""
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()

		