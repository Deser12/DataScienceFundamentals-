#import the Json library
import json

#Open Json file and attaching it to the movies variable
with open("movies.json") as f: 
	movies = json.load(f)

#Create a function, so we can loop this program over. 
def choice():

#ask for user for their choice 
	user_choice = int(input("What do you want to do? \n 1. Filter by year \n 2. Search for movies where the director is also an actor \n 3. Filter by certain genre  \n 4. Search for movies shorter than 2hr \n 5. Close this program"))

	# is the user choice is one execute this lines of code
	if user_choice == 1: 
		#ask the users for a year they want to filter by
		user_year = input("Name a year")
		#loop thru the movies and assign the title and year to the variables
		for movie in movies:
			title = movie["title"]
			year = movie["year"]

			#if the variable year is equal to the year (input by user) than the title should be printed.
			if year == int(user_year):
				print("\n" + title)
		#the program should be running till the user chooses to quit the program. 
		choice() 
	elif user_choice == 2: 
		
		for movie in movies: 
			title = movie["title"]
			director = movie["director"]
			actor = movie["actors"]

			if director in actor:
				print("\n" + title)
		choice()
	elif user_choice == 3:
		user_genre = input("Name a genre")
		user_genre

		for movie in movies:
			title = movie["title"]
			genre = movie["genres"]

			if user_genre in genre:
				print("\n" + title)
		choice()

	elif user_choice == 4: 

		for movie in movies:
			title = movie["title"]
			duration = movie["duration"]


			if duration <= 120:
				print("\n" + title)
		choice()

	elif user_choice == 5: 
		exit()

	else: 
		print("Wrong choice :) ")
		choice();

choice()
