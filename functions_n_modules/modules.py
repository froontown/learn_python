# You can export functions in a separate file called a module
# Then, you can import the module!

# Importing whole modules:
# Pretend we've got a file called 'pizza.py' with the following functions in there:
def make_pizza(size, *toppings):
	"""Summarize the pizza we're making"""
	print(f"Making a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")


# In a separate file, 'making_pizzas.py', we can do this:
import pizza

# The syntax works like: call the module, then the module's function:
# Think: moduleName.functionName()

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushroom', 'sausage', 'rhino')

# Importing specific functions:
from module_name import function_0, function_1, function_2

# Using our 'pizza.py' example:
from pizza import make_pizza

# You don't need the '.' notation
make_pizza(16, 'pepperoni')

# You can give a function an alias if it's name is the same as something else in the program you're importing into:
# Pretend the program we're importing 'pizza.py' into has a function called `make_pizza()`
from pizza import make_pizza as mp

# then call it like this:
mp(16, 'giraffes')

# You can give a module an alias, too:
import pizza as p

p.make_pizza(16, 'wildebeasts')

# Importing all functions in a module, but this is not recommended since it can cause a lot of conflict:
from pizza import *

