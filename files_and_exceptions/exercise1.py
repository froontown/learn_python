filename = 'learning_python.txt'

print("Just printing the whole thing.\n")
with open(filename) as file_object:
	contents = file_object.read()
	print(contents)

print("====")
	
print("Just printing teach line.\n")
with open(filename) as file_object:
	for line in file_object:
		print(line)

print("====")

print("Making a list first, then printing the list out.")
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line)


with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	line = line.rstrip()
	print(line.replace('Python', 'WOO!!!'))

	# can do this, too:
for line in lines:
    # Get rid of newline, then replace Python with C.
    print(line.rstrip().replace('Python', 'C'))