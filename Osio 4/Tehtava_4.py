import random

print("Tässä pelissä arvataan kokonaislukuja väliltä 1-10! Peli kertoo jokaisen arvauksen jälkeen arvasitko ala- vai yläkanttiin.")

while True:

    luku = random.randint(1, 10)

    while True:
        arvaus = int(input("Anna arvauksesi: "))
        if arvaus > luku:
            print("Luku on pienempi kuin arvauksesi")
        elif arvaus < luku:
            print("Luku on suurempi kuin arvauksesi")
        elif arvaus == luku:
            print("Arvasit oikein, voitit pelin!")
            break
        else:
            continue

    while True:                                                         #tarkistetaan antaako käyttäjä validin vastauksen jatkolle
        vastaus = input("Haluatko pelata uudestaan? kyllä/ei: ")
        if vastaus.casefold() == "kyllä" or "ei":
            break
        else:
            continue

    if vastaus.casefold() == "ei":                                      #tarkistetaan jatkaako pelaaja vai lopetetaanko peli
        print("Peli lopetettu.")
        break
    elif vastaus.casefold() == "kyllä":
        continue



