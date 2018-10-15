
friends = [
	{
		"name" : "Barrie",
		"age" : 24
	}, 
	{
		"name" : "Tinus",
		"age" : 25
	},
	{
		"name" : "Tina",
		"age" : 26
	},
]

for friend in friends:
	name = friend["name"]
	print(f"{name}, {len(name)}")
	snack = input("What's your favorite snack?")
	friend["snack"] = snack  
	
print(friends
