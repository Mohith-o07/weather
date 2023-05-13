import requests
import json
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
if __name__ == "__main__":
    print("Weather info, created by Mohith E")
    city = input("Enter the name of the city: ")
    url = f"https://api.weatherapi.com/v1/current.json?key=636ef8376e934f55885144623230505&q={city}"
    r = requests.get(url)
    # print(r.text)
    dictw = json.loads(r.text)
    temp = dictw["current"]["temp_c"]
    humid = dictw["current"]["humidity"]
    feels_like = dictw["current"]["feelslike_c"]
    text = f"current temperature in {city} is {temp} degrees celcius, feels like {feels_like} degrees celcius with {humid} percent humidity."
    print(text)
    speak.Speak(text)
