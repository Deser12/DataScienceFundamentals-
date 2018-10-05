friends = [
		["Tinus", 24],
		["Barrie", 25],
		["Tina", 26]
]


for friend in friends: 
	print(friend[0])
	print(len(friend[0]))
	ask_snack = input("What is your favorite snack?")
	friend.append(ask_snack)


print(friends)
