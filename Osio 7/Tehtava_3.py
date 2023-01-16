print("Tervetuloa lentokenttätietokantaan, voit käyttää tietokantaa seuraavilla komennoilla: \
'Hae', 'Lisää', 'Lopeta'")

db = {}

cmd = input("Anna komento:")

while cmd != "Lopeta":
    if cmd == "Lisää":
        # print("lisays")
        nimi = input("Anna lentokentän nimi: ")
        koodi = input("Anna lentokentän ICAO-koodi: ")
        db[koodi] = nimi
    elif cmd == "Hae":
        koodi = input("Anna lentokentän ICAO-koodi: ")
        print(f"Koodia vastaava lentokenttä on: {db[koodi]}")
        # print("Haku")
    # elif cmd == "Lopeta":  # tällä hetkellä taitaa olla turha mut antaa nyt olla
    #     print("Heippa!")
    #     break
    else:
        print("Komentoa ei tunnistettu, yritä uudelleen.")
    cmd = input("Anna komento: ")
    if cmd == "Lopeta":
        print("Heippa!")
