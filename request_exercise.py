import requests

urls = input("Type in a url").strip()

r = requests.get(urls)

if r.status_code != 200:
	print("Error")
	exit()
else: 
	print(r.status_code)

for key, value in r.headers.items(): 
	print(f"{key} :  {value}")



text_list = r.text.split("\n")
counter = 0

while counter <= 10:
	print(text_list[counter])
	counter +=1
