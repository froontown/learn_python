message = "Hello world!"
print(message)

message = "This is a new value"
print(message)

# Capitalize:
name = "froon the town"
print(name.title())

# All caps:
name = "froon the town"
print(name.upper())

# All lower:
name = "FROON THE TOWN"
print(name.lower())

# Concatenating:
first_name = "froon"
last_name = "town"
full_name = first_name + " " + last_name
print(full_name.title())

# Whitespace things:

# New Line: \n
# Tab: \t

# Get rid of whitespace:
this_language = "Python "
print(this_language.rstrip())

# Change type:
age = 23

# This won't work:
# message = "Happy " + age + "rd Birthday!"

# To change the int to a str:

message = "Happy " + str(age) + "rd Birthday!"
print(message)

# Lists are Arrays
a = ['star', 'nebula', 'planet', 'dark matter']
print(a)
print(a[0])
print(a[-1])
print(a[1].title())

# Changing elements in an array:
a[0] = 'comet'
print(a)

a.append('asteroid')
print(a)

a.insert(1, 'black hole')
print(a)

del a[0]
print(a)

popped_a = a.pop()
print(a)
print(popped_a)

popped = a.pop(2)
print(popped)
print(a)

a.remove('dark matter')
print(a)

# Other methods;

b = ['star', 'asteroid', 'comet', 'black hole', 'nebula', 'planet', 'moon']
print(sorted(b)) # Temporarily sorts an array
b.sort() # Permanently sorts alphabetically
print(b)

b.reverse()
print(b)

len(b) # Length of the list
print(len(b))