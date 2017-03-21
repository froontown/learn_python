# Moving an item from one list to another:

newPeople = ['Katherine', 'Ben', 'Liz', 'JP', 'Froon']
setPeople = []

while newPeople:
	currentPerson = newPeople.pop()

	print(f"Verifying person: {currentPerson}")
	setPeople.append(currentPerson)

# Removing instances of an item in a list/array:
pets = ['dog', 'cat', 'fish', 'monkey', 'cat', 'hippo', 'tiger', 'cat']

while 'cat' in pets:
	pets.remove('cat')

print(pets)

# Fill a hash/dictionary with User input:
responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
	# Prompt for the person's name and response:
	name = input("\nWhat's your name? ")
	response = input("Which mountain would you like to climb today? ")

	# Store the response in the dictionary:
	responses[name] = response

	# Find out if anyone else is going to take the poll.
	repeat = input("Would you like to let another person erspond? (yes/no) ")
	if repeat == 'no':
		polling_active = False

# Polling is complete. Show the results:
print("\n--- Poll Result ---")
for name, response in responses.items():
	print(f"{name} would like to climb {response}.")
