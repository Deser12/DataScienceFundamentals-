#import the csv module used in line 84
import csv

#open the csv file in 'read' modus and attach the data to the politicians variable
politicians = open("politicians.csv", "r")
politician_list = []

#loop thru the csv file using the enumerate function
for index, politician in enumerate(politicians):
	#split and strip all data and add it to the variable politican_list
	politician_list.append(politician.strip().split(","))
#since i don't need this file for now, i can close it. 
politicians.close()

#Loop thru the politican list using the enumerate function
for index, politician in enumerate(politician_list): 

	#use the index variable to locate the correct data in the politician list and attach it to the right variable
	name = politician_list[index][0] 
	surname = politician_list[index][1]
	birth_year = politician_list[index][2]
	party = politician_list[index][3]

	#print these variables in a correct sentence.
	print(str(index) + ": " + name + " "+ surname + " is born in " + birth_year + " and is a member of the " + party + " party.")

# i choose to create a function here, so i can recall this function later on, to keep this program running. 
def choices():
	#print the various options in the terminal
	print(" A few options: \n 1: Do you want to remove a person? \n 2: Do you want to add a person? \n 3: Save the csv file? \n 4: Exit the program")
	#use the user_input to determine which part of the program to run
	user_input = input(" \n Type the number of your option")

	#if the user pressed option 1
	if int(user_input) == 1: 
		#ask the user which politician they want to remove
		user_choice1 = input("Type the number of the politician you want to remove")
		#use the pop function to delete the chosen politician
		politician_list.pop(int(user_choice1))

		#Just to give the user good feedback i will print this list again
		for index, politician in enumerate(politician_list): 

			name = politician_list[index][0] 
			surname = politician_list[index][1]
			birth_year = politician_list[index][2]
			party = politician_list[index][3]

			print(str(index) + ": " + name + " "+ surname + " is born in " + birth_year + " and is a member of the " + party + " party.")
		#keep the main function running till the user choose to end the program. 
		choices()

	#if the user pressed option 1
	elif int(user_input) == 2: 
		#ask the user which politician they want to add
		name = input("What's the name of the politician?")
		#append this name as a new [item] in the list
		politician_list.append([name])
		surname = input(f"What's {name}'s surname?")
		birth_year = input(f"What's {name} {surname}'s birth_year?")
		party = input(f"What's {name} {surname}'s party?")

		#Since i added a new item above i can just append this information to the last (-1) list item 
		politician_list[-1].append(surname)
		politician_list[-1].append(birth_year)
		politician_list[-1].append(party)

		#Just to give the user good feedback i will print this list again
		for index, politician in enumerate(politician_list): 

			name = politician_list[index][0] 
			surname = politician_list[index][1]
			birth_year = politician_list[index][2]
			party = politician_list[index][3]

			print(str(index) + ": " + name + " "+ surname + " is born in " + birth_year + " and is a member of the " + party + " party.")	
		#keep the main function running till the user choose to end the program. 
		choices()

	#if the user pressed option 3
	elif int(user_input) == 3: 
		#open the csv file and attach the data to politicians		
		with open("politicians.csv", 'w') as politicians: 
			#create an variable and add the csv.writer function to it.
			a = csv.writer(politicians)
			#use this variable to write the items of politician list to the rows in the csv
			a.writerows(politician_list)
			#give the user feedback that the saving is finished.
			print("Done! \n")
		#keep the main function running till the user choose to end the program. 
		choices()

	#if the user pressed option 3
	elif int(user_input) == 4: 
		#use the exit function to exit the program
		exit()

	#if the user pressed a number that is not in the list (1-4) they get the chance to try it again and again. 
	else: 
		print("Wrong choice, Try again!")
		choices()

choices()
