print("Tervetuloa lentokenttätietokantaan, voit käyttää tietokantaa seuraavilla komennoilla: \
'Hae', 'Lisää', 'Lopeta'")

cmd = input("Anna komento:")

while cmd != "Lopeta":
    if cmd == "Lisää":
        print("lisays")
    elif cmd == "Hae":
        print("Haku")
    elif cmd == "Lopeta":
        break
    else:
        print("Komentoa ei tunnistettu, yritä uudelleen.")
    cmd = input("Anna komento: ")
