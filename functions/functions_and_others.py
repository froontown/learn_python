# Functions and while loops:

def getFormattedName(firstName, lastName):
	"""Return a full name, formatted."""
	fullName = f"{firstName} {lastName}"
	return fullName.title()

while True:
	print("Please tell me your name: ")
	print("Press 'q' to quit.")
	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break


	formattedName = getFormattedName(f_name, l_name)
# 	print(f"Hello, {formattedName}!")

# Functions and Lists

# Passing a list:
def greet_users(names):
	"""Print a simple greeting to each user in the list."""
	for name in names:
		msg = f"Hello, {name.title()}!"
		print(msg)

usernames = ['froon', 'honey', 'piccolo']
greet_users(usernames)


# Modifying a list:
# We've got a list of things that we want to "build."
unprinted_models = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Go through each `unprinted_model` and "build it"
while unprinted_models:
	current_design = unprinted_models.pop()

	# Print/build the item:
	print(f"Printing model: {current_design}")
	completed_models.append(current_design)

# Display the completed models:
print("The following models have been completed: ")
for completed_model in completed_models:
	print(completed_model)
print(completed_models)

# Refactoring using two functions:

def print_models(unprinted_designs, completed_models):
	"""
	Simulate printing each design until none are left.
	Move each design to completed_models after printing.
	"""

	while unprinted_designs:
		current_design = unprinted_designs.pop()

		# Simulate creating a 3D print from the design.
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""Show all the models that were printed."""

	print("\nThe following models have been printed: ")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['car', 'battery', 'bracelet', 'human soul']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# If you don't want to lose the original list, (in this case, `unprinted_designs`,) copy it first:
print_models(unprinted_designs[:], completed_models)



