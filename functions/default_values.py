# Default values
# Define the parameter while defining the function:

def defaultDog(petName, petType = 'dog'):
	"""Display info about a pet"""
	print(f"I have a {petType}.")
	print(f"My {petType}'s name is {petName.title()}.")

defaultDog('snoopy')
defaultDog(petName = 'snoopy')

# To override the default parameter:
defaultDog('chester', petType = 'cheetah')
defaultDog('chester', 'cheetah')
defaultDog(petName = 'chester', petType = 'cheetah')

