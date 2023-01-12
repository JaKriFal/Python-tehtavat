
def galtol(arg):
    litrat = arg*3.785
    return litrat

x = float(input("Anna gallonamäärä: "))

while x >= 0:
        print(f"Litramäärä on {galtol(x)}")
        x = float(input("Anna gallonamäärä: "))

print("Suoritus lopetettu")
