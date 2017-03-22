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