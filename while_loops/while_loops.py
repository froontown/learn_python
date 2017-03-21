# While loops:
num = 1
while num <= 10:
	print(num)
	num += 1
	
# User decides when to quit:

prompt = "I'll repeat what you say: "
prompt += "\nEnter 'quit' to stop."

message = ""

while message != 'quit':
	message = input(prompt)
	print(message)

	if message != 'quit':
		print(message) # prevents it from printing "quit"

# Flags:

prompt = "I'll repeat what you say: "
prompt += "\nEnter 'quit' to stop."

active = True
while active:
	message - input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)

# Using a break:

prompt = "Give me a city name: "
prompt += "\nEnter 'quit' when you're done."

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print(f"I'd love to go to {city}!")

# Continue in a loop:

num = 0
while num < 10:
	num += 1
	if num % 2 == 0:
		continue

	print(num)

