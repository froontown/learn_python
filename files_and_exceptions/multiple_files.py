# We've moved a bunch of stuff from 'filenotfound.py' to here and put it all in one function:

def count_words(file):
	"""Count the approximate number of words in a file."""
	try:
		with open(file) as f:
			contents = f.read()
	except FileNotFoundError:
		msg = f"Sorry - a file named {file} does not exist."
		print(msg)
	else: 
		words = contents.split()
		num_words = len(words)
		print(f"The file {file} has about {num_words} words.")
	
# Now, if we have more than one text, we can count 'em each up!

filenames = ['samples/alice.txt', 'samples/missingfile.txt', 'samples/grimms.txt', 'samples/hans.txt']
for filename in filenames:
	count_words(filename)

# If you want the program to fail silently, (not provide an error message and move along like nothing happened,) put `pass` in the `except` block:

# def count_words(file):
# 	"""Count the approximate number of words in a file."""
# 	try:
# 		with open(file) as f:
# 			contents = f.read()
# 	except FileNotFoundError:
# 		msg = f"Sorry - a file named {file} does not exist."
# 		print(msg)
# 	else: 
# 		pass

# filenames = ['samples/alice.txt', 'samples/missingfile.txt', 'samples/grimms.txt', 'samples/hans.txt']
# for filename in filenames:
# 	count_words(filename)
