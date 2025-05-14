import requests

url = "https://simple-chatgpt-api.p.rapidapi.com/ask"

payload = {'Question: What type of work environment do you prefer? answered as: Quiet and focused.'
		   'Question: How do you handle challenges at work? answered as: Taking charge independently.'
		   'Question: What is your preferred work schedule? answered as: Standard 9 to 5.'
		   'This prompt is sent to chatgpt api, what is missing here? What to do to make it more efficient?'}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "MY API KEY WAS HERE",
	"X-RapidAPI-Host": "simple-chatgpt-api.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())