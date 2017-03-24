# NOTE: different modes:
	# r = read mode
	# w = write mode
	# a = append mode
	# r+ = read/write mode

# Let's write to a file, 'programming.txt'

filename = 'programming.txt'

with open(filename, 'w') as file_object:
	# We're opening `filename`
	# The 'w' means we're opening it in "write mode" 
	file_object.write("I fucking love programming!")
	file_object.write("\nThis is a new line.")


# Appending to a file:
with open(filename, 'a') as file_object:
	file_object.write("I am appended, yo.\n")
	file_object.write("I'm going to be the best web developer in the world!")

