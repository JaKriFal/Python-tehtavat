pituus = float(input("Anna kuhan pituus senttimetreinä: "))

if 37 > pituus > 0:
    print(f"Kuhasi on {37-pituus:6.2f} cm alamittainen, päästä se takaisin!")
elif pituus >= 37:
    print("Kuhasi on täysimittainen")
else:
    print("Ohjelma ei tunnistanut kuhasi mittaa tai kerroit aikamoisen kalavaleen!")
