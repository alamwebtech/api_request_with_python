import requests 
user_input = input("What would you like to search for? ")

url = "https://icanhazdadjoke.com/search"

res=requests.get(
	url,
	 headers={"Accept":"application/json"},
	 params={"term":user_input}
).json()

num_jokes = res["total_jokes"]
if num_jokes > 1:
	print("There are many jokes")
elif num_jokes == 1:
	print("There is one joke")
else: 
	print("There are no jokes ")

# print(num_jokes)