nimet = set()

nimi = input("Syötä nimi: ")

while nimi != "":
    test = len(nimet)
    nimet.add(nimi)
    nimi = input("Syötä nimi:")
    if nimi == "":
        break
    elif nimi in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi.")

print("Syötetyt nimet olivat:")
for n in nimet:
    print(n)

