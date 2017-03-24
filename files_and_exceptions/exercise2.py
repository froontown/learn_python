name = input("Yo gimme your name: ")

with open('guest.txt', 'w') as file_object:
	file_object.write(name)

print("====")

print("Enter 'quit' when you're done.")

while True:
	name_2 = input("What is your name, dawg? ")
	if name_2 == 'quit':
		break
	else:
		with open('guestbook.txt', 'a') as file_object:
			file_object.write(name_2 + "\n")
		print(f"Sup, {name_2}. You are now on the list.")

filename = 'programming_poll.txt'

responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(response + "\n")