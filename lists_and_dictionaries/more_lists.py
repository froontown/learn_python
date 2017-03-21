aa = ['star', 'nebula', 'black hole', 'planet', 'asteroid', 'comet'] 

for a in aa:
	print(a)

for a in aa:
	print("A " + a.title() + " is an object in space!")
print("That's all objects in space.")

for value in range(1,5):
	print(value)
	# outputs: 1, 2, 3, 4

nums = list(range(1,6))
print(nums)

even_nums = list(range(2,11,2))
	# Starts at `2`, then adds 2 until it reaches `11
print(even_nums)

# Printing a buncha squared numbers, 1-10:
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)

print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Can refactor:
squares2 = []
for value in range(1,11):
	squares2.append(value**2)

print(squares2)

# Simple Stats:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehension:
squared = [value**2 for value in range(1,11)]
print(squared)

# Slicing a list:
print(digits[0:3])
print(digits[2:10])
print(digits[:4])
print(digits[2:])
print(digits[-3:])

# Loop through a slice:
for digit in digits[:3]:
	print(digit)

# Copying a list:
copied_digits = digits[:]
print(copied_digits)

# Tuples
rectangle = (200, 50)