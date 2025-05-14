import requests

url = "https://simple-chatgpt-api.p.rapidapi.com/ask"

payload = { "question": "what is javascript?" }
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "MY API KEY WAS HERE",
	"X-RapidAPI-Host": "simple-chatgpt-api.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())