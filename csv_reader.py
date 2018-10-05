footballers = open("footballers.csv", "r")
f = open("new_file.txt", "w")

for player in footballers:
	player_list = player.strip().split(",")
	player_name = player_list[0]
	player_club = player_list[1]
	player_price = player_list[2]
	player_price = int(player_price + "000000")
	print(player_name + " is a player of " + player_club + ". Costs: €" + str(player_price))
	f.write(player_name + " is a player of " + player_club + ". Costs: €" + str(player_price)+ " \n")

footballers.close()

