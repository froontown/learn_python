# We're going to be working with 'pi_digits.txt' here:

# The program below opens and reads the file then prints it out to the console:
with open('pi_digits.txt') as file_object:
	# `with()` opens and closes a file on its own - you COULD use `open()` and `close()`, but improperly closing a file can lead to problems.
	# `open('pi_digits.txt')` opens the file in the given directory
	# `as file_object` stores the opened file into `file_object` for later
	contents = file_object.read()
	# We use `read()` to read through `file_object` and store that into the variable `contents`
	print(contents)

	# Can read a file line by line:

filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())
			# Since `print()` adds a `\n` automatically, using `.rstrip()` will get rid of that extra line

# Accessing things with `with` makes those things only available within that `with` block
# To make them accessable outside the block, store it in a variable:

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())

# Let's mess with pi!!!

pi_string = ''
for line in lines:
	pi_string += line.rstrip()
		# Here we're adding each line and stripping the `\n` each time

print(pi_string)
print(len(pi_string))

# This outputs with two empty spaces because of the way 'pi_digits.txt' is formatted. to get rid of them, we can do this
pi_string_formatted = ''
for line in lines:
	pi_string_formatted += line.strip()

print(pi_string_formatted)