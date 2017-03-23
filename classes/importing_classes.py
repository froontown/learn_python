# Notice we have 'Car.py' in the same folder
# Let's import that class!

from car import Car
my_car = Car('toyota', '4runner', 2006)
print(my_car.get_descriptive_name())

my_car.odometer_reading = 500
my_car.read_odometer()

# See? Neat!

# You can store multiple classes in a "Module". By adding more classes to 'Car.py', you can import more classes from a module like:

from car import ElectricCar

# Now we can do something like this:

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Importing multiple classes:

from car import Car, ElectricCar

# Importing a whole Module:
import car

# Importing all the classes from a module:

from car import *

# Importing a module into a module:
# Just import the module into the module you're making. When creating something in a new file, you just need to import from each module separately.
