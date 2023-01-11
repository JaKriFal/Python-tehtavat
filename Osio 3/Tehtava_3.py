suk = input("Anna sukupuoli muodossa 'Nainen' tai 'Mies': ")
hemo = float(input('Anna hemoglobiiniarvo muodossa g/l: '))

if suk.casefold() == "mies":

    if 134 <= hemo <= 195:
        print("Hemoglobiinisi on normaali.")
    elif 0 < hemo < 134:
        print("Hemoglobiinisi on alhainen.")
    elif hemo > 195:
        print("Hemoglobiinisi on liian korkea.")
    else:
        print("Jokin meni pieleen, kokeile uudestaan.")

if suk.casefold() == "nainen":

    if 117 <= hemo <= 175:
        print("Hemoglobiinisi on normaali.")
    elif 0 < hemo < 117:
        print("Hemoglobiinisi on alhainen.")
    elif hemo > 175:
        print("Hemoglobiinisi on liian korkea.")
    else:
        print("Jokin meni pieleen, kokeile uudestaan.")





