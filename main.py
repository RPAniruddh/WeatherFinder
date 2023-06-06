import requests
import json
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

city = input("Enter the city :- ")
url = f"https://api.weatherapi.com/v1/current.json?key=3ae3dea5a8864fd6bf2140701230606&q={city}"

r = requests.get(url)
weather = json.loads(r.text)

text = f"The Temperature of {city} is {weather['current']['temp_c']}"
print(text)
speak.Speak(text)