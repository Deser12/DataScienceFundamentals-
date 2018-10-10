import requests
import json
import webbrowser

user_input = input("Name an article").strip()

user_input = user_input.replace(" ", "_")

def check(language):
	url = f"https://{language}.wikipedia.org/api/rest_v1/page/summary/{user_input}"

	req = requests.get(url)

	data = json.loads(req.text)

	if req.status_code == 200:
			print(data["title"])
			print("\n")
			if "description" in data:
				print(data["description"])
				print("\n")
			print(data["extract"])
			print("\n")
	else: 
		print("Wrong article")

language = ["en", "fr", "de"]
for lang in language:
	check(lang)

user_ask = input("Want to open the article in the browser? \n Y/N?")

if user_ask == "Y" or "y":
	webbrowser.open(f'https://wikipedia.org/wiki/{user_input}')

else: 
	exit()

