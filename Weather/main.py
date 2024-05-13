import json
import pyttsx3
import requests

engine = pyttsx3.init()

city_name = input("Enter the city you want to know about.")
r = requests.get(f"https://api.weatherapi.com/v1/current.json?key=afb0d57da4154a4e88c81038241502&"
                 f"q={city_name.capitalize()}&api=yes")

print(r.text)

wea = json.loads(r.text)

print(wea["location"]["name"])
temp = wea["current"]["temp_c"]
engine.say(f"The temperature in {city_name} is {temp} degree celsius.")
engine.runAndWait()
