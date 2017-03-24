# Adding numbers and accounting for User not inputting actual digits:

print("Give me two numbers and I'll add them!: ")
print("Press 'q' to quit.")

while True:
	try:
		first_num = input("First number: ")
		if first_num == 'q':
			break

		first_num = int(first_num)

		second_num = input("Second number: ")
		if second_num == 'q':
			break

		second_num = int(second_num)

	except ValueError:
		print("It must be a number, 0-9!")

	else:
		sum = first_num + second_num
		print(f"The sum of {first_num} and {second_num} is {sum}.")

print('=====')
# Going through file documents and printing their contents, verifying if a file even exists, too.
files = ['samples/cats.txt', 'samples/sunbro.txt', 'samples/dogs.txt']

for file in files:
	print(f"Reading {file}...")
	try:
		with open(file) as f:
			contents = f.read()
			print(contents.title())
	except FileNotFoundError:
		print("Cannot find that file.")
		pass

print('=====')

file = 'samples/grimms.txt'

with open(file) as f:
	contents = f.read()
	contents.lower().count('the')
	