# Let's return some values, sonn!!!

def getFormattedName(firstName, lastName):
	"""Return a full name, neatly fortmatted."""
	fullName = f"{firstName} {lastName}"
	return fullName.title()

musician = getFormattedName('froon', 'town')
print(musician)

# Let's return a dictionary!!!

def build_person(firstName, lastName):
	"""Return a dictionary of a person."""
	person = {
		'first': firstName,
		'last': lastName,
		}
	return person

musician = build_person('jimi', 'hendrix')
print(musician)

# Let's add some more to `build_person`

def build_person(firstName, lastName, age=''):
	"""Return a dictionary of a person."""
	person = {
		'first': firstName,
		'last': lastName,
		}
	if age:
		person['age'] = age

	return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)