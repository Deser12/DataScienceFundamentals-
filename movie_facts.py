movies = {
	"Title" : "Blade Runner",
	"Year" : 1982,
	"Duration" : 117,
	"Director" : "Ridley Scott"

}
#add minutes to the Duration value
movies["Duration"] = f'{movies["Duration"]} minutes'
 
#create a list in the dictionary
movies["actors"] = ["Harrisson Ford", "Rutger Hauer", "Sean Young"]

#Add a comma after the actornames
movies["actors"] = ", ".join(movies["actors"])

for key, value in movies.items(): 
	print(f"{key} :  {value}")
	





