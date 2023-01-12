f = True

while f :
    x = float(input("Anna tuumamäärä: "))
    if x < 0:
        break
    else:
        print(f"{x} tuumaa on {x*2.54:6.2f} cm.")

