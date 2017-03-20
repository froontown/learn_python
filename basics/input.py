# Messing with `input()`
message = input("Imma repeat what you say:")
print(message)

# Multi-line:
prompt = "We want your name."
prompt += "\nWhat's your name? "
name = input(prompt)
print(f"\nHello, {name}!")

# Taking integers as input so you can do stuff with it:

message = input("How old are you? ")
message = int(message)
print(message)

if message >= 21:
	print("\nYou can drink booze!")
else:
	print("\nGet outta here, kid.")

# Some challenges here:
car = input("What kind of car would you like?")
# What kind of car would you like? Honda
print(f"Let me find a {car} for you.")
# Let me find a  Honda for you.
party = input("How many people are in your party? ")
# How many people are in your party? 5
party = int(party)
party
# 5
if party >= 4:
    print("You've got at least a party of 5!")
else:
    print("Your party isn't a TV show.")
# You've got at least a party of 5!
num = input("Give me a number! ")
# Give me a number! 47
num = int(num)
if num % 10 == 0:
    print("That's divisible by 10!")
else:
    print("Yo that isn't divisible by 10!")
# Yo that isn't divisible by 10!

# While loops:
num = 1
while num <= 10:
	print(num)
	num += 1
	