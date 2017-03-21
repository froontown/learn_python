# Position Arguments

def describe_pet(animalType, petName):
	"""Display info about a pet."""
	print(f"I have a {animalType}.")
	print(f"My {animalType}'s name is {petName.title()}.")

describe_pet('dog', 'piccolo')

# Keyword Arguments

def describe_animal(animal, name):
	"""Display info about an animal"""
	print(f"I have a {animal}.")
	print(f"My {animal}'s name is {name.title()}.")

describe_animal(animal='cheetah', name='chester') # This is the same as:
describe_animal(name='chester', animal='cheetah')


# Optional arguments:

def fullName(firstName, lastName, middleName = ''):
	"""Returns a formatted, full name."""
	if middleName:
		full_name = f"{firstName} {middleName} {lastName}"
	else:
		full_name = f"{firstName} {lastName}"
	return full_name.title()

musician = fullName('jimi', 'hendrix')
print(musician)

musician2 = fullName('john', 'hooker', 'lee')
print(musician2)
