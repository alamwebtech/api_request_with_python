import requests 
import pyfiglet
from random import choice


user_input = input("What would you like to search for? ")


header = pyfiglet.figlet_format(user_input)
print(f"{header} jokes")

url = "https://icanhazdadjoke.com/search"

res=requests.get(
	url,
	 headers={"Accept":"application/json"},
	 params={"term":user_input}
).json()

num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1:
	print(f"I found {num_jokes} jokes about {user_input}. Here is one:")
	print(choice(results)["joke"])
elif num_jokes == 1:
	print(f"I found one joke about {user_input}")
	print(results[0]["joke"])
else: 
	print(f"There are no jokes with yoour term: {user_input}")

# print(num_jokes)