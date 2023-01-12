
luvut = []

x = input("Anna ensimmäinen kokonaisluku tai lopeta painamalla Enter: ")

while x != "":
    luvut.append(int(x))
    x = input("Anna kokonaisluku tai tai lopeta painamalla Enter: ")

luvut.sort(reverse = True)

print(f"Viisi suurinta lukua olivat seuraavat: {luvut[0:5]}")

