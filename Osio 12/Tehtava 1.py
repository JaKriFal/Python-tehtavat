import json
import requests

pyynto = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(pyynto)
    if vastaus.status_code == 200:
        jsonvastaus = vastaus.json()
        print(jsonvastaus["value"])

except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa")


