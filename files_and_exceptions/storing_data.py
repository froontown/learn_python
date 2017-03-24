# Welcome to the wonderful world of JSON

# # This program stores a set of numbers:
# import json
# 	# We're importing the json module

# numbers = [2, 3, 5, 7, 11, 13]
# 	# Making a list of numbers

# file = 'numbers.json'
# 	# We're going to write to this file

# with open(file, 'w') as f:
# 	json.dump(numbers, f)
# 		# this stores the list 'numbers' in 'numbers.json'

print('=====')

# Now, let's read that data
import json
	# import the module json

file = 'numbers.json'
	# store the file into 'file'

with open(file) as f:
	numbers = json.load(f)
	# open the file and store its contents into numbers

print(numbers)