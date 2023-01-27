import json
import requests

query = input("Anna paikkakunnan nimi: ")

pyynto = "http://api.openweathermap.org/geo/1.0/direct?q="+ query +"&limit=5&appid=55cff1485baee5623423b4e365e15aef"

try:
    vastaus = requests.get(pyynto)
    if vastaus.status_code == 200:
        print("Toimii!")
        jsonvastaus = vastaus.json()
        saapyynto = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(jsonvastaus[0]["lat"]) + "&lon=" +\
                    str(jsonvastaus[0]["lon"]) + "&appid=55cff1485baee5623423b4e365e15aef"
        saa = requests.get(saapyynto)
        if saa.status_code == 200:
            json_saa = saa.json()
            saatyyppi = json_saa["weather"][0]["description"]
            celsius = float(json_saa["main"]["temp"]) - 273.15
            print(f"Säätyyppi: {saatyyppi}, lämpötila: {celsius}")



except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa")