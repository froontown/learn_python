# Let's pretend we're accessing a file that doesn't exist.
# This'll return a "FileNotFoundError"
# f = 'alice.txt'

# with open(f) as file:
# 	context = file.read()

# Let's fix it up with a try-except block~

file = 'alice.txt'

try:
	with open(file) as f:
		contents = f.read()
except FileNotFoundError:
	msg = f"Sorry - a file named {file} does not exist."
	print(msg)

# Okay so now 'alice.txt' exists. let's play some more:

# Analyzing text:
else: 
	# Count the approx. num of words in the file:
	words = contents.split()
	num_words = len(words)
	print(f"The file {file} has about {num_words} words.")