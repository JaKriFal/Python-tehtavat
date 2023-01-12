import math

def pizzacalc(d, e):
    a = math.pi * ((d/2)**2)
    am = a/10000
    return e/am



pizza1h = float(input("Anna pizzan 1 hinta: "))
pizza1d = float(input("Anna pizzan 1 halkaisija: "))
pizza2h = float(input("Anna pizzan 2 hinta: "))
pizza2d = float(input("Anna pizzan 2 halkaisija: "))

if pizzacalc(pizza1d, pizza1h) > pizzacalc(pizza2d, pizza2h):
    print("Pizza 2 on halvempi!")
else:
    print("Pizza 1 on halvempi!")





