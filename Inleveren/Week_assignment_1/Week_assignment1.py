#Welcome statement
print("Welcome!")

#Asking the user' name and adding it in a welcome statement
name = input("What's your first name?")
print("Welcome " + name + ", to my program!")

#asking for the last name and checking if it matches mine (in both capitalized or all lower case). 
last_name = input("what is your last name?")

if last_name.lower().strip() == "vieira":
	print("Hey! me might be family")
else: 
	print(name + " " + last_name +". Interesting name!.")

# ask for birth year and also convert it to an integer.
birth_year = int(input("So, what's your birth year?"))

#substracting current year with the birth year to get the age (not accurately)
age = 2018 - birth_year

#Checking if the age is greater than, or equal to 18. If the user is older, continue with the script. If they are younger, alert that the program will quit, and quit the program)

if age >= 18:
	print("You are old enough to use this social network")
elif age < 0: 
	print("Ha, that must be wrong! But hey still too young, try again!")
	exit(0)

else: 
	print("Alert. You are not old enough! This program will close itself.")
	exit(0)



Social_media_value = 0
# Collect the information of question 1 into variable city. This is needed to calculate the estimated value
city = input("So, " + name +" " + last_name + ", Where do you live?")

if city.lower().strip() == 'rotterdam': 
	print("Rotterdam... Nice. Me too!")

else: 
	print(city + "... Nice!")

if city.lower().strip() == "rotterdam":
	Social_media_value += 3 

elif city.lower().strip() == "utrecht":
	Social_media_value += 2 

else: 
	Social_media_value += 1 
# Collect the information of question 1 into variable movie. This is needed to calculate the estimated value
social_media = input("Quick question, What social media do you use the most?")

#Deciding which social media is worth points 
if social_media.lower().strip() == "facebook":
	Social_media_value += 4 
elif social_media.lower().strip() == "instagram":
	Social_media_value += 3 
elif social_media.lower().strip() == "twitter":
	Social_media_value += 2 
else :
	Social_media_value += 1

print(social_media + ".. Thats cool!")

phone_usage = int(input("How many hours per day do you use your phone?"))	

if phone_usage >= 8: 
	Social_media_value += 4
	print(str(phone_usage) + "!!!! You need help!")
elif phone_usage > 5 and phone_usage <8:
	Social_media_value += 3
elif phone_usage < 5 and phone_usage >2: 
	Social_media_value += 2 
else : 
	Social_media_value += 1 

social_media_label = ""

if Social_media_value == 11:
	social_media_label = "Very useful"
elif Social_media_value > 5 and Social_media_value <11:
	social_media_label = "useful"
else:
	social_media_label = "useless"
#The social value is the length of each data point + 3 times the age. Return this value to the user.

print(f"\n  So  {name} {last_name}, You are {age} years old and you live in {city}. You are mostly active on {social_media} and you user your phone for {phone_usage} hours per day. Your social media value is {Social_media_value}. That means that your value is  {social_media_label}. Goodbye!")






