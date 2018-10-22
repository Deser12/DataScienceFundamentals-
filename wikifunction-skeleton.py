"""
To see an example of the Wikipedia API JSON look at this url:
https://en.wikipedia.org/api/rest_v1/page/summary/Japanese_cuisine
"""
import requests

def input_user(title, value):
	url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
	req = requests.get(url)

	if req.status_code != 200:
	    print(f"We got an error: {req.status_code}")
	    exit() 
		
	data = req.json()
	new_data = (data[f"{value}"])
	return new_data

title = input("What title you want to see?").strip()
value = input("What's your value?").strip().lower()
data = input_user(title, value)
print(data)

