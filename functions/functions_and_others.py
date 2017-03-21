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
	print(f"Hello, {formattedName}!")