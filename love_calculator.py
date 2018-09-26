import random

own_name = input("What's your name?")
lover_name = input("What's your lovers name?")

name_strip = own_name.strip()
lover_strip = lover_name.strip() 

name_lower = name_strip.lower()
lover_lower = lover_strip.lower()

name = len(name_lower)
lover = len(lover_lower)

random_low_number = random.randint(1, 33)
random_mid_number = random.randint(34, 66) 
random_high_number = random.randint(67, 100) 

if name > lover:
	print("Too bad " + str(random_low_number) +"%")
elif name == lover: 
	print("Nice Try " + str(random_mid_number) +"%")
else:
	print("Go for it " + str(random_high_number) +"%")







