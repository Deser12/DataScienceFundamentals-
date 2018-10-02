friends_names = ["Barrie", "Tinus", "Tina"]
friend_ages = [24, 25, 26]
friends_snack = []

for names in friends_names: 
	# print(names)
	# # printing the length of the names
	# print(str(len(names)) + " letter name")

	#adding the input of the snacks into the empty friends snack list 
	friends_snack.append(input(names + " (" + str(len(names)) + ")" + " What's your favorite snack?"))

#Creating a variable called index to resemble the place in the list
index = 0

for names in friends_names:
	# print names + the items in the list friends_snack using the index code that is defined above this section
	print(names + ", Your favorite snack is " + friends_snack[index])

	#add 1 to the index each time the loops run through the code 
	index += 1
 


