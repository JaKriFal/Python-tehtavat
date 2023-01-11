
i = 0

while i < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    if (tunnus == "python") and (salasana == "rules"):
        print("Tervetuloa!")
        break
    elif i == 4:
        print("Pääsy evätty!")
        break
    else:
        i += 1
        print(f"Sinulla on vielä {5-i:2} kirjautumisyritystä jäljellä.")
        continue



