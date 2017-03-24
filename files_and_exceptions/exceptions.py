# As an example, we'll contrive an error by dividing by zero:

# print(5/0)

# This yields:
# Traceback (most recent call last):
#   File "exceptions.py", line 3, in <module>
#     print(5/0)
# ZeroDivisionError: division by zero

# try:
# 	print(5/0)
# except ZeroDivisionError:
# 	print("You can't divide by zero!")

# # Preventing Crashes:
# # A good example is User input: Users often input something the program doesn't expect.
# # Below, if a User uses '0' as the second_number, then things go bad:
# print("Give me two numbers and I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
# 	first_number = input("\nFirst number: ")
# 	if first_number == 'q':
# 		break
# 	second_number = input("\nSecond Number: ")
# 	if second_number == 'q':
# 		break
# 	answer = int(first_number) / int(second_number)
# 	print(answer)

# So! Let's use a try-except block!

print("Give me two numbers and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("\nSecond Number: ")
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("you can't divide by zero!")
	else:
		print(answer)
