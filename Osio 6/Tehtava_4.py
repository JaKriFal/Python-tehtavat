def summari(arg):
    summa = 0
    for x in arg:
        summa = summa + x
    return summa


# Pääohjelma:

lista = [1, 3, 4, 5, 6, 7, 8]

print(f"Lista: {lista}")
print(f"Listan summa: {summari(lista)}")
